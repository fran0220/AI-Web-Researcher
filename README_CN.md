# AI 网络研究助手

## 快速开始

### 1. 环境配置
```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# Linux/Mac 系统:
source venv/bin/activate
# Windows 系统:
# .\venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置设置
在项目根目录创建 `.env` 文件并配置 API 密钥：
```env
# API 密钥配置
# 阿里云通义千问 API（OpenAI 兼容接口）
OPENAI_API_KEY=your_qwen_api_key
OPENAI_API_BASE=https://dashscope.aliyuncs.com/compatible-mode/v1

# 搜索提供商 API 密钥（可选）
TAVILY_API_KEY=your_tavily_key
BRAVE_API_KEY=your_brave_key
BING_API_KEY=your_bing_key
EXA_API_KEY=your_exa_key
```
注意：
- 项目现已支持通过 OpenAI 兼容接口使用阿里云通义千问模型
- 如果未提供搜索提供商密钥，将默认使用 DuckDuckGo
- 推荐使用 qwen-long 模型，可在保持良好性能的同时提供更好的成本效益

### 3. 运行应用
```bash
# 方式1：直接运行（确保环境变量已设置）
python Web-LLM.py

# 方式2：使用提供的脚本（自动加载 .env 文件）
chmod +x run.sh
./run.sh
```

### 使用方法
- 研究查询以 '@' 开头
  示例：`@分析人工智能对医疗保健的影响`
- 按 CTRL+D (Linux/Mac) 或 CTRL+Z (Windows) 提交输入
- 研究过程中可用命令：
  - 's'：显示当前研究进度
  - 'f'：显示当前研究重点领域
  - 'q'：退出研究并生成总结
- 研究结果将自动保存到文本文件中

## 项目描述
AI 网络研究助手是一个创新的研究助手工具，它利用大型语言模型（包括阿里云通义千问）进行全面的自动化在线研究。与传统的 LLM 交互不同，该工具通过将查询分解为重点研究领域，系统地进行网络搜索和网页内容提取，并将所有发现的内容和来源链接编译成文本文档。

## 主要特性

### 研究能力
1. 自动研究规划：
   - 将研究查询分解为5个重点领域
   - 基于相关性分配优先级
   - 根据发现调整研究重点

2. 多源搜索：
   - 支持多个搜索提供商（Tavily、Brave、Bing、Exa）
   - DuckDuckGo 作为备选方案
   - 自优化搜索机制

3. 内容处理：
   - 系统化网页抓取
   - 相关信息提取
   - 来源 URL 记录
   - 自动内容组织

4. 交互控制：
   - 实时进度监控
   - 重点领域检查
   - 研究终止与总结
   - 研究后问答功能

### 技术特性
- 支持多个 LLM 提供商：
  - 阿里云通义千问（推荐：qwen-long，成本效益好）
  - OpenAI API 兼容端点
  - 通过 Ollama 支持本地 LLM
- 自动文档记录和来源追踪
- 丰富的控制台输出和状态指示
- 综合答案合成
- 研究对话模式

## 工作原理

1. 查询分析：
   - 用户输入研究查询（如："@分析人工智能对医疗保健的影响"）
   - 系统分析并将查询分解为具体研究领域

2. 系统研究：
   - 对研究领域进行优先级排序
   - 制定针对性搜索查询
   - 在多个提供商中进行网络搜索
   - 提取和验证相关信息

3. 文档记录：
   - 自动保存所有发现
   - 记录来源 URL
   - 维护研究进度
   - 生成综合总结

4. 交互功能：
   - 实时状态更新
   - 重点领域检查
   - 研究控制命令
   - 研究后讨论

本工具的关键特点在于它不仅仅是一个聊天机器人，而是一个能够系统性研究主题并维护文档记录的自动化研究助手。您可以让它运行并返回查看，就能得到一份包含大量相关网站内容的综合文档，并附有完整的来源归属。

## 更新和改进
- 添加了对阿里云通义千问模型的支持
- 通过使用 qwen-long 模型优化了成本效益
- 增强了文档和使用说明
- 改进了错误处理和系统初始化

## 项目演示

[![项目演示](https://img.youtube.com/vi/hS7Q1B8N1mQ/0.jpg)](https://youtu.be/hS7Q1B8N1mQ "项目演示")

点击上方图片观看项目演示。

## 安装说明

1. 克隆仓库：
```sh
git clone https://github.com/fran0220/AI-Web-Researcher.git
cd AI-Web-Researcher
```

2. 按照"快速开始"部分的说明进行环境配置和运行。

## 贡献
欢迎提交问题报告和改进建议，让我们一起使这个 AI 研究助手变得更强大！
