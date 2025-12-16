# 最简单的AI试卷插件
# 用法：AI可以直接读取这个文件，或者调用其中的函数

# 直接读取整个文件
def read_exam_simple(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

# 使用
exam_content = read_exam_simple("test1.txt")

# 简单的函数接口
def get_exam_content():
    """返回完整的试卷内容"""
    return exam_content

def search_question(keyword):
    """搜索包含关键词的题目"""
    lines = exam_content.split('\n')
    results = []
    for i, line in enumerate(lines):
        if keyword.lower() in line.lower():
            results.append(f"第{i+1}行: {line}")
    return results

def get_question_by_number(number):
    """获取指定题号的题目"""
    # 简单查找题号
    import re
    pattern = rf"{number}\.\s+(.*?)(?=\n\d+\.|\Z)"
    match = re.search(pattern, exam_content, re.DOTALL)
    if match:
        return f"{number}. {match.group(1)}"
    return "未找到该题目"

# 直接运行测试
if __name__ == "__main__":
    print("=== AI试卷插件 ===")
    print("可用的函数:")
    print("1. get_exam_content() - 获取完整试卷")
    print("2. search_question('关键词') - 搜索题目")
    print("3. get_question_by_number(1) - 获取第1题")