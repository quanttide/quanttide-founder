import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


def get_base_url():
    lark_env = os.getenv("LARK_ENV", "feishu")
    if lark_env == "lark":
        return "https://open.larksuite.com"
    return "https://open.feishu.cn"


def get_tenant_access_token():
    app_id = os.getenv("FEISHU_APP_ID")
    app_secret = os.getenv("FEISHU_APP_SECRET")
    base_url = get_base_url()

    resp = requests.post(
        f"{base_url}/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": app_id, "app_secret": app_secret},
    )
    data = resp.json()
    if data.get("code") != 0:
        raise Exception(f"Failed to get tenant token: {data}")
    return data.get("tenant_access_token")


def list_space_nodes(token, space_id, parent_node_token=None):
    base_url = get_base_url()
    url = f"{base_url}/open-apis/wiki/v2/spaces/{space_id}/nodes"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"page_size": 50}
    if parent_node_token:
        params["parent_node_token"] = parent_node_token

    resp = requests.get(url, headers=headers, params=params)
    return resp.json()


def get_space_info(token, space_id):
    base_url = get_base_url()
    url = f"{base_url}/open-apis/wiki/v2/spaces/{space_id}"
    headers = {"Authorization": f"Bearer {token}"}

    resp = requests.get(url, headers=headers)
    return resp.json()


def main():
    space_id = os.getenv("FEISHU_WIKI_SPACE_ID")
    if not space_id:
        print("请设置 FEISHU_WIKI_SPACE_ID")
        return

    token = get_tenant_access_token()
    print(f"API: {get_base_url()}")
    print(f"知识库 ID: {space_id}\n")

    info = get_space_info(token, space_id)
    if info.get("code") == 0:
        print(f"知识库名称: {info['data']['name']}")
        print(f"知识库描述: {info['data'].get('description', '无')}")
        print()

    result = list_space_nodes(token, space_id)
    if result.get("code") == 0:
        items = result.get("data", {}).get("items", [])
        print(f"根节点数量: {len(items)}")
        print("\n目录结构:")
        for node in items:
            print(f"  - {node.get('title')} ({node.get('obj_type')})")
            if node.get("has_child"):
                children = list_space_nodes(token, space_id, node.get("node_token"))
                if children.get("code") == 0:
                    for child in children["data"]["items"]:
                        print(f"    └─ {child.get('title')} ({child.get('obj_type')})")
    else:
        print(f"Error: {result.get('msg')}")


if __name__ == "__main__":
    main()
