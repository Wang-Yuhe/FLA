#!/usr/bin/env python3
"""
检查项目依赖是否已安装
"""

import sys

def check_module(name, import_name=None):
    """检查模块是否已安装"""
    if import_name is None:
        import_name = name

    try:
        __import__(import_name)
        print(f"✓ {name} 已安装")
        return True
    except ImportError:
        print(f"✗ {name} 未安装")
        return False

def main():
    print("=" * 50)
    print("检查项目依赖")
    print("=" * 50)
    print()

    modules = [
        ("numpy", "numpy"),
        ("scipy", "scipy"),
        ("matplotlib", "matplotlib"),
        ("pptree", "pptree"),
    ]

    results = []
    for name, import_name in modules:
        results.append(check_module(name, import_name))

    print()
    print("=" * 50)

    if all(results):
        print("✓ 所有依赖已安装！可以运行项目了。")
        return 0
    else:
        print("✗ 缺少部分依赖，请安装：")
        print()
        print("安装方法1（推荐）:")
        print("  pip3 install numpy scipy matplotlib pptree")
        print()
        print("安装方法2（如果遇到SSL问题）:")
        print("  pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org numpy scipy matplotlib pptree")
        print()
        print("安装方法3（使用requirements.txt）:")
        print("  pip3 install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())

