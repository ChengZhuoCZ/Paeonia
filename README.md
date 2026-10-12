# Paeonia

**Paeonia** 是 `math-manuscript-reconstructor` skill 的发布仓库，用于数学研究论文的重构写作、局部润色和参考文献审计。

当前版本：**v1.42.0**。仓库名称为 Paeonia；skill 内部名称保留为 `math-manuscript-reconstructor`，以保持原始包及其引用路径完整。

## 功能

- 在摘要、引言、定理、证明和备注之间保持统一的研究数学语言风格。
- 区分全文或指定区域的重构与局部润色，保留数学命题的适用范围和受保护的文本。
- 根据数学对象、领域习惯和公式可读性选择记号，并检查重复或冲突。
- 在适用时研究相关数学文献、核对具体定理及其假设，并据此组织引言和证明引用。
- 提供协议、检查清单、模板、辅助工具与回归测试。

普通写作默认以用户提供的证明为数学输入；独立的证明正确性审计需要另行明确请求。

## 下载与安装

从 [v1.42.0 Release](https://github.com/ChengZhuoCZ/Paeonia/releases/tag/v1.42.0) 下载 `math-manuscript-reconstructor-v1.42.0.skill`。

- 支持 `.skill` 文件导入的客户端：使用客户端的 skill 导入功能。
- 使用目录形式的客户端：将文件按 ZIP 格式解压，把完整的 `math-manuscript-reconstructor/` 目录放入客户端指定的 skills 目录。
- 从源码安装：使用本仓库的 [`skills/math-manuscript-reconstructor/`](skills/math-manuscript-reconstructor/) 目录。

安装时保留 `SKILL.md` 和同级资源目录。完整使用说明见 [skill README](skills/math-manuscript-reconstructor/README.md)，入口见 [SKILL.md](skills/math-manuscript-reconstructor/SKILL.md)。

## v1.42.0

本版本引入统一的数学论文语言风格，不再默认要求选择作者范例或提供多种文风选项。原有的编辑范围约束、精确到定理的文献引用和语义记号选择机制继续保留。

详细变化见 [CHANGELOG](skills/math-manuscript-reconstructor/CHANGELOG.md)。原包的验证范围与限制见 [VALIDATION](skills/math-manuscript-reconstructor/VALIDATION.md)。

## 仓库结构

```text
Paeonia/
├── README.md
├── skills/
│   └── math-manuscript-reconstructor/  # 原始包解压后的全部内容
└── dist/
    ├── math-manuscript-reconstructor-v1.42.0.skill
    └── SHA256SUMS
```

## 完整性

`dist/` 中的 `.skill` 文件与提供的原始文件逐字节一致，解压后的 741 个文件也保持原样。发布前已核对包内清单的 739 条 SHA-256 记录，全部匹配；这项检查验证文件完整性，不代表对实际数学论文质量或外部引用适用性的重新审计。

下载发行文件及同一 Release 的 `SHA256SUMS` 后，可在它们所在的目录中校验：

```bash
shasum -a 256 -c SHA256SUMS
```

原始文件 SHA-256：

```text
e826c96e228ef060e18e05b81963f6c7a6e5128943b455c75aa3ef4c9f3e016b
```
