import sys
import json

SITE_DATA = {
    "title": "爱游戏门户",
    "url": "https://portalhome-aiyouxi.com.cn",
    "keywords": ["爱游戏", "门户", "游戏资讯", "玩家社区"],
    "tags": ["游戏", "门户网站", "中文"],
    "description": "面向爱游戏用户的综合门户站点，提供游戏动态、社区互动与资源导航。"
}

def format_summary(data: dict) -> str:
    """从站点数据生成结构化摘要文本"""
    lines = []
    lines.append(f"站点名称：{data['title']}")
    lines.append(f"URL：{data['url']}")
    lines.append(f"关键词：{', '.join(data['keywords'])}")
    lines.append(f"标签：{', '.join(data['tags'])}")
    lines.append(f"简介：{data['description']}")
    return "\n".join(lines)

def to_json_block(data: dict) -> str:
    """将站点数据格式化为JSON块（用于展示）"""
    return json.dumps(data, ensure_ascii=False, indent=2)

def print_summary(style: str = "text"):
    """根据指定样式输出摘要"""
    if style == "json":
        print(to_json_block(SITE_DATA))
    else:
        print(format_summary(SITE_DATA))

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        print_summary("json")
    else:
        print_summary("text")

if __name__ == "__main__":
    main()