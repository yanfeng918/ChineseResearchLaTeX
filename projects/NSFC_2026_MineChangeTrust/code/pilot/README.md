# MCT-P01：公开矿山变化检测预实验

使用作者公开的 MineNetCD256 裁切版本，检验训练与评测链路，并比较无一致性约束、全区域约束、仅训练背景约束。详细结果见[预实验报告](../../docs/06_公开数据预实验.md)。本实验是小规模探索，未复现原论文全部基线，未评价官方测试集。

## 数据与许可

- 原始记录：<https://rodare.hzdr.de/record/3251>，DOI `10.14278/rodare.3251`。
- 作者裁切版：<https://huggingface.co/datasets/HZDR-FWGEL/MineNetCD256>，由原始记录链接。
- Yu, Zhang, Gloaguen, Zhu, Ghamisi；MineNetCD；CC BY 4.0。派生示例图中的预测为本次运行生成，来源影像与标签按上游许可署名。
- 仅下载三个训练分片、一个验证分片，共1,408,512,171字节。`data_sources.json`固定文件名、字节数与SHA256；URL指向main时仍强制校验这些固定哈希，不默默接收更新后的文件。
- 60个官方训练矿区划出50个用于本预实验、10个保留；仅从50矿区抽取1,188片。10个官方验证矿区抽取480片。全部影像为256×256，二值标签中非零为变化。30个官方测试矿区影像不下载、不读取、不评分。

## 复现

Python 3.11.15、PyTorch 2.5.1+cu121、CUDA 12.1、单张NVIDIA A40。其他实际版本见`requirements.txt`。需安装与本机驱动匹配的PyTorch CUDA构建；不同硬件或软件版本不保证逐位相同。CPU运行未验证。

在仓库根目录确定绝对路径，然后切换至测试工作区执行；模型、数据与中间文件不写入源码目录：

```bash
REPO="$(pwd)"
PILOT_CODE="$REPO/projects/NSFC_2026_MineChangeTrust/code/pilot"
mkdir -p "$REPO/tests/nsfc-2026-minechangetrust/pilot-reproduction"
cd "$REPO/tests/nsfc-2026-minechangetrust/pilot-reproduction"
python "$PILOT_CODE/download_data.py" --data-dir data/hf
python "$PILOT_CODE/prepare_data.py" --data-dir data/hf --output-dir cache
python "$PILOT_CODE/select_examples.py" --cache-dir cache
CUDA_VISIBLE_DEVICES=0 python "$PILOT_CODE/run_pilot.py" --cache-dir cache --output-dir runs
python "$PILOT_CODE/summarize_results.py" --cache-dir cache --run-dir runs --output-dir summary
```

原始运行目录为`tests/nsfc-2026-minechangetrust/pilot-20260906/`。轻量结果、样本来源清单、冻结配置、日志摘要与复算审计存于本目录`results/`；完整权重和像素预测保留在原始运行目录。下载脚本在已有文件上验证成功；原始网络下载记录也保留在运行目录。不得把一次成功运行表述为上游服务永远可用。

## 约定与边界

`protocol.json`在训练前固定抽样、三组、种子17/29/43、12轮、阈值0.5及统计口径。每组同一种子使用相同初始化、批次顺序和同步翻转；全部九个末轮模型保存后才统一评估验证集。恢复训练时核对代码、配置、样本和缓存哈希；不依据验证结果选轮次或追加参数搜索。

每矿区先汇总像素计数，再等权平均有效矿区。无真变化时IoU/F1/召回记NA；无预测正例时精确率记NA；无背景时FPR记NA。小变化仅为原生切片内面积不超过64像素、不接触边界的8连通标签区，统计其像素召回；该阈值不代替正式项目的小变化定义。

误差条是三个种子的样本标准差。差异区间先在每矿区平均种子，再对矿区配对bootstrap 10,000次，取95%百分位区间；不是把30个“矿区×种子”当独立样本。区间为探索性，不能替代正式检验、非劣界和多重比较处理。

仅背景约束使用训练标签构造掩码，验证前向输入只有两时相影像。没有完整近邻复现、随机掩码、强度匹配、概率校准或复核效用实验，不能单凭这三组证明新机制或可靠性增益。保留所有种子和负结果。当前只有矿区ID及完全重复影像对审计，未完成地理邻近、切片重叠、配准和标签语义的专业核验。
