# Paeonia

**Paeonia** 是用于数学研究论文重构写作、局部润色和参考文献审计的 skill。

当前版本：**v1.43.0**。展示名称为 **Paeonia**；安装标识、内部名称和目录为 `paeonia`，可通过 `$paeonia` 调用。

## 功能

- 在摘要、引言、定理、证明和备注之间保持统一的研究数学语言风格。
- 区分全文或指定区域的重构与局部润色，保留数学命题的适用范围和受保护的文本。
- 根据数学对象、领域习惯和公式可读性选择记号，并检查重复或冲突。
- 在适用时研究相关数学文献、核对具体定理及其假设，并据此组织引言和证明引用。
- 从数学内容与论证出发审读全文，检查重复表达、空泛过渡、公式复述和缺乏依据的重要性表述。
- 对生成的 LaTeX 稿件实施禁止视觉框的排版约束，并提供能够检查本地引用文件的源码扫描工具。
- 提供协议、检查清单、模板、辅助工具与回归测试。

普通写作默认以用户提供的证明为数学输入；独立的证明正确性审计需要另行明确请求。

## 下载与安装

从 [v1.43.0 Release](https://github.com/ChengZhuoCZ/Paeonia/releases/tag/v1.43.0) 下载 `Paeonia-v1.43.0.skill`。

- 支持 `.skill` 文件导入的客户端：使用客户端的 skill 导入功能。
- 使用目录形式的客户端：将文件按 ZIP 格式解压，把完整的 `paeonia/` 目录放入客户端指定的 skills 目录。
- 从源码安装：使用本仓库的 [`skills/paeonia/`](skills/paeonia/) 目录。

安装时保留 `SKILL.md` 和同级资源目录。更新已安装的版本时，请用新目录替换旧版 skill，避免重复加载。完整使用说明见 [skill README](skills/paeonia/README.md)，入口见 [SKILL.md](skills/paeonia/SKILL.md)。

## v1.43.0

本版本新增全文语言审读协议与检查清单，结合数学论证检查重复措辞、证明节奏和跨章节回声。新增禁止视觉框的排版协议、独立发布门槛、源码扫描与语言审读工具；源码扫描支持检查本地引用文件。已有的统一语言风格、编辑范围约束、精确到定理的文献引用和语义记号选择继续保留。

语言诊断提供需要审读的位置，不判定作者身份或给出“AI 百分比”；源码扫描也不等同于对生成 PDF 的视觉检查。

详细变化见 [CHANGELOG](skills/paeonia/CHANGELOG.md)。验证范围与限制见 [VALIDATION](skills/paeonia/VALIDATION.md)。

## 仓库结构

```text
Paeonia/
├── README.md
├── skills/
│   └── paeonia/                       # skill 入口及完整资源
└── dist/
    ├── Paeonia-v1.43.0.skill
    └── SHA256SUMS
```

## 完整性

`dist/` 中的 `.skill` 文件与提供的 v1.43.0 原始文件逐字节一致，解压后的 767 个文件与 `skills/paeonia/` 逐文件一致。发布前已核对包内两份清单的全部 765 条 SHA-256 记录，并通过 skill 格式校验与完整发布测试套件。发行文件的校验值见 `dist/SHA256SUMS`，包内验证报告见 [VALIDATION](skills/paeonia/VALIDATION.md)。

下载发行文件及同一 Release 的 `SHA256SUMS` 后，可在它们所在的目录中校验：

```bash
shasum -a 256 -c SHA256SUMS
```
