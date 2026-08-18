const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, BorderStyle, WidthType, ShadingType,
  VerticalAlign, PageNumber, HeadingLevel,
} = require("docx");

const A4_W = 11906;
const A4_H = 16838;
const MARGIN = 1134; // 2cm
const CONTENT_W = A4_W - MARGIN * 2; // 9638

const thin = { style: BorderStyle.SINGLE, size: 8, color: "000000" };
const borders = { top: thin, bottom: thin, left: thin, right: thin };
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };
const cellMargins = { top: 60, bottom: 60, left: 80, right: 80 };

function font(text, opts = {}) {
  return new TextRun({
    text,
    font: { ascii: "Times New Roman", eastAsia: "SimSun", hAnsi: "Times New Roman" },
    size: opts.size || 24, // 12pt
    bold: !!opts.bold,
    italics: !!opts.italics,
    color: opts.color || "000000",
  });
}

function p(text, opts = {}) {
  const runs = Array.isArray(text) ? text : [font(text, opts)];
  return new Paragraph({
    alignment: opts.align || AlignmentType.JUSTIFIED,
    spacing: { after: opts.after ?? 120, line: opts.line ?? 360 },
    indent: opts.indent ? { firstLine: 480 } : undefined,
    children: runs,
  });
}

function center(text, opts = {}) {
  return p(text, { ...opts, align: AlignmentType.CENTER });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    outlineLevel: 0,
    spacing: { before: 240, after: 160 },
    children: [font(text, { size: 32, bold: true })],
  });
}

function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    outlineLevel: 1,
    spacing: { before: 200, after: 120 },
    children: [font(text, { size: 28, bold: true })],
  });
}

function cell(text, width, opts = {}) {
  const children = Array.isArray(text)
    ? text.map((t) => (typeof t === "string" ? p(t, { after: 60, indent: opts.body }) : t))
    : [p(text, { after: 40, align: opts.align, bold: opts.bold, indent: opts.body })];
  if (opts.bold && !Array.isArray(text)) {
    children[0] = new Paragraph({
      alignment: opts.align || AlignmentType.LEFT,
      spacing: { after: 40 },
      children: [font(String(text), { bold: true, size: opts.size || 21 })],
    });
  }
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    columnSpan: opts.span || 1,
    borders,
    margins: cellMargins,
    verticalAlign: VerticalAlign.CENTER,
    shading: opts.shade ? { type: ShadingType.CLEAR, fill: opts.shade } : undefined,
    children,
  });
}

function row(cells) {
  return new TableRow({ children: cells });
}

function table(columnWidths, rows) {
  return new Table({
    width: { size: columnWidths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths,
    rows,
  });
}

const cover = [
  center("编号（由实验室填写）______________", { size: 21, after: 200 }),
  center("中央民族大学", { size: 44, bold: true, after: 80 }),
  center("“民族语言智能分析与安全治理”教育部重点实验室", { size: 32, bold: true, after: 80 }),
  center("开放课题申请书", { size: 44, bold: true, after: 80 }),
  center("（2026年度）", { size: 28, bold: true, after: 400 }),
  p("课题名称：场景文字增强的维吾尔语多模态表征融合与跨语言图像理解", { after: 160 }),
  p("申 请 者：颜丰", { after: 160 }),
  p("工作单位：新疆大学", { after: 160 }),
  p("联系电话：【待填】", { after: 160 }),
  p("电子邮箱：【待填】", { after: 160 }),
  p("申请日期：2026年8月", { after: 400 }),
  center("二○二六年制", { size: 28, bold: true, after: 0 }),
];

const infoCols = [1800, 1400, 1000, 1000, 1400, 1000, 1038, 1000];
// simplify basic info as stacked labeled table with 2-3 columns
const c2 = [2400, CONTENT_W - 2400];
const c3 = [1800, 3019, 1800, 3019];

const basicInfo = [
  h1("一、课题基本信息表"),
  table([2400, CONTENT_W - 2400], [
    row([cell("课题名称", 2400, { bold: true, shade: "F2F2F2" }), cell("场景文字增强的维吾尔语多模态表征融合与跨语言图像理解", CONTENT_W - 2400)]),
  ]),
  table([1800, 1600, 1600, 1600, 1500, 1538], [
    row([
      cell("申请金额（万元）", 1800, { bold: true, shade: "F2F2F2" }),
      cell("5.00", 1600),
      cell("起止年月", 1600, { bold: true, shade: "F2F2F2" }),
      cell("2027年1月至2028年12月", 1600 + 1500 + 1538, { span: 3 }),
    ]),
  ]),
  table([1200, 1400, 1000, 1200, 1400, 1400, 2038], [
    row([
      cell("申请者", 1200, { bold: true, shade: "F2F2F2" }),
      cell("姓名", 1400, { bold: true, shade: "F2F2F2" }),
      cell("颜丰", 1000),
      cell("性别", 1200, { bold: true, shade: "F2F2F2" }),
      cell("【待填】", 1400),
      cell("出生年月", 1400, { bold: true, shade: "F2F2F2" }),
      cell("【待填】", 2038),
    ]),
    row([
      cell("", 1200, { shade: "F2F2F2" }),
      cell("专业技术职务", 1400, { bold: true, shade: "F2F2F2" }),
      cell("副教授", 1000),
      cell("学位", 1200, { bold: true, shade: "F2F2F2" }),
      cell("博士", 1400),
      cell("最终学位授予机构", 1400, { bold: true, shade: "F2F2F2" }),
      cell("【待填】", 2038),
    ]),
  ]),
  table(c2, [
    row([cell("工作单位", 2400, { bold: true, shade: "F2F2F2" }), cell("新疆大学", CONTENT_W - 2400)]),
    row([cell("联系地址", 2400, { bold: true, shade: "F2F2F2" }), cell("【待填】", CONTENT_W - 2400)]),
    row([cell("E-MAIL", 2400, { bold: true, shade: "F2F2F2" }), cell("【待填】", CONTENT_W - 2400)]),
    row([cell("联系电话", 2400, { bold: true, shade: "F2F2F2" }), cell("【待填】", CONTENT_W - 2400)]),
  ]),
  table([CONTENT_W], [
    row([cell("课题组主要成员：总人数共（1）人，其中：高级职称（1）人，中级职称（0）人，初级职称（0）人，博士后（0）人，研究生（0）人，其他（0）人。研究生可参与实验，未列入签字栏的人员不作为正式成员。", CONTENT_W)]),
  ]),
  table([1400, 800, 1200, 1600, 1800, 1600, 1238], [
    row([
      cell("姓名", 1400, { bold: true, shade: "F2F2F2" }),
      cell("性别", 800, { bold: true, shade: "F2F2F2" }),
      cell("出生年月", 1200, { bold: true, shade: "F2F2F2" }),
      cell("专业技术职务", 1600, { bold: true, shade: "F2F2F2" }),
      cell("工作单位", 1800, { bold: true, shade: "F2F2F2" }),
      cell("课题中的分工", 1600, { bold: true, shade: "F2F2F2" }),
      cell("签章", 1238, { bold: true, shade: "F2F2F2" }),
    ]),
    row([
      cell("颜丰", 1400),
      cell("【待填】", 800),
      cell("【待填】", 1200),
      cell("副教授", 1600),
      cell("新疆大学", 1800),
      cell("主持，总体设计、方法实现与论文撰写", 1600),
      cell("", 1238),
    ]),
  ]),
  table(c2, [
    row([
      cell("研究内容摘要", 2400, { bold: true, shade: "F2F2F2" }),
      cell("本课题面向低资源维吾尔语自然场景图像，研究场景文字视觉编码与图像外观、维/汉描述的异构特征融合，形成可检验的跨语言图像—文本检索与小规模图像理解评价。以公开数据集 SUST/RUST 与 Multi30k-Distant 为主评测，不建设翻译系统、语音系统或舆情平台。预期在两年内完成方法、对照与消融，并力争发表中科院三区及以上 SCI 论文 1 篇，实验室为第一署名单位。", CONTENT_W - 2400),
    ]),
    row([
      cell("关键词", 2400, { bold: true, shade: "F2F2F2" }),
      cell("民族语言多模态融合；维吾尔语场景文字；跨语言图像理解；跨模态检索；低资源表征学习", CONTENT_W - 2400),
    ]),
  ]),
];

const section2 = [
  h1("二、立论依据"),
  h2("1. 课题研究目的、意义及应用前景"),
  p("民族地区自然场景图像往往同时包含物体外观和场景文字。路牌、招牌、海报上的维吾尔语既标识地点与商户，也构成图像语义的一部分。现有视觉—语言模型主要在英文或中文图文对上训练，倾向于回答“图中是什么”，对黏着语、从右向左书写、连写变体丰富的维吾尔语场景文字缺乏稳定编码。若把这类图像只当作一般照片做跨模态检索，文字通道被当成纹理；若只做场景文字识别，又丢掉物体与场景上下文。", { indent: true }),
  p("本项目面向实验室“民族语言多模态提取融合”方向，研究如何把维吾尔语场景文字作为独立视觉语言通道，与图像外观、维吾尔语描述和汉语描述一并编码，并在公开可核验数据上检验跨语言图像—文本检索与小规模图像理解。对象收敛到维—汉图文，不扩展为通用民汉翻译系统、语音交互或舆情治理。实验室开放课题经费有限、周期两年，可检验的交付是：在公开数据上复现基线、加入文字通道、报告检索与消融。", { indent: true }),
  h2("2. 国内外研究概况、水平和发展趋势"),
  p("视觉—语言对比学习把图像与句子拉到共享空间，CLIP、ALIGN 与 SigLIP 提供了可迁移的图文编码器；SCAN、ALBEF、BLIP 等进一步做细粒度对齐或统一理解。这些模型的训练数据以自然描述为主，图像中的文字通常不被单独建模。把 CLIP 式编码器直接零样本用于维—汉检索，只能作为对照，不能当作已经解决场景文字问题。", { indent: true }),
  p("场景文字识别把“图中的字”当作序列转写问题。CRNN、ABINet、TrOCR 与 CLIP4STR 把识别从序列标注推进到语言校正和视觉—语言预训练。TextVQA、ST-VQA 与 OCR-VQA 表明：当答案写在图里时，只看物体外观不够。但 STR 输出字符串，图像理解需要的是可融合的连续向量。若只把识别结果再翻译成汉语再检索，错误会在 OCR、翻译和检索三级累积。", { indent: true }),
  p("多语 CLIP（AltCLIP、mCLIP、Chinese CLIP 等）很少把维吾尔语当作主测试语言。视觉枢纽研究表明共享图像可以缓解缺少句对时的跨语言对齐；Multi30k-Distant 把 Multi30k 人工译成汉语和维吾尔语，但任务是多模态翻译而不是场景文字增强的图像理解。SUST/RUST 提供维语场景文字公开数据，验收仍是识别准确率。CUTE 与 MC² 可作文本预训练，CUTE 含机器翻译生成部分，不作图像理解金标准。", { indent: true }),
  p("现有不足可以概括为三条。第一，图文检索缺少维吾尔语场景文字通道。第二，维语 STR 停在识别准确率，没有检验文字特征是否改善跨语言检索。第三，视觉枢纽工作面向翻译，缺少以 Recall@K、MRR 和去掉文字通道消融为主的图像理解验收。本项目以“场景文字编码—异构融合—跨语言检索与理解评价”为主线，对照包括通用多语 CLIP 零样本、无文字通道对比学习、OCR 后翻译再检索。", { indent: true }),
  h2("3. 主要参考文献"),
  p("[1] Radford A, et al. Learning Transferable Visual Models From Natural Language Supervision. ICML, 2021."),
  p("[2] Chen Z, et al. AltCLIP: Altering the Language Encoder in CLIP for Extended Language Capabilities. ACL Findings, 2023."),
  p("[3] Chen G, et al. mCLIP: Multilingual CLIP via Cross-lingual Transfer. ACL, 2023."),
  p("[4] Shi B, Bai X, Yao C. An End-to-End Trainable Neural Network for Image-Based Sequence Recognition and Its Application to Scene Text Recognition. IEEE TPAMI, 2017."),
  p("[5] Fang S, et al. Read Like Humans: ABINet for Scene Text Recognition. CVPR, 2021."),
  p("[6] Zhao S, et al. CLIP4STR: A Simple Baseline for Scene Text Recognition With Pre-Trained Vision-Language Model. IEEE TIP, 2024."),
  p("[7] Singh A, et al. Towards VQA Models That Can Read. CVPR, 2019."),
  p("[8] Biten A F, et al. Scene Text Visual Question Answering. ICCV, 2019."),
  p("[9] Huang P-Y, et al. Unsupervised Multimodal Neural Machine Translation with Pseudo Visual Pivoting. ACL, 2020."),
  p("[10] Tayir T, et al. Visual Pivoting Unsupervised Multimodal Machine Translation in Low-Resource Distant Language Pairs. EMNLP Findings, 2024."),
  p("[11] Kong F, et al. SUST and RUST: Two Datasets for Uyghur Scene Text Recognition. IEEE Access, 2023."),
  p("[12] Yang W, et al. Collaborative Encoding Method for Scene Text Recognition in Low Linguistic Resources: The Uyghur Language Case Study. Applied Sciences, 2024."),
  p("[13] Zhang C, et al. MC²: Towards Transparent and Culturally-Aware NLP for Minority Languages in China. ACL, 2024."),
  p("[14] Zhuang W, Sun Y. CUTE: A Multilingual Dataset for Enhancing Cross-Lingual Knowledge Transfer in Low-Resource Languages. COLING, 2025."),
  p("[15] Elliott D, et al. Multi30K: Multilingual English-German Image Descriptions. VL Workshop, 2016."),
  p("[16] Yan F, et al. Knowledge-Aware Image Understanding with Multi-Level Visual Representation Enhancement for Visual Question Answering. Machine Learning, 2024."),
  p("[17] Yan F, et al. SPCA-Net: a based on spatial position relationship co-attention network for visual question answering. The Visual Computer, 2022."),
  p("[18] Xu P, Yan F, et al. RSHR+: Progressive question-conditioned visual calibration and structured state-space reasoning for remote sensing visual question answering. Expert Systems with Applications, 2026."),
  p("（其余条目见 LaTeX 工作区 references/myexample.bib，共 41 条可核验文献。）"),
];

const section3 = [
  h1("三、研究方法"),
  h2("1. 研究内容、预期目标和拟解决的关键问题"),
  p("内容一：维吾尔语场景文字视觉编码。在 SUST 上训练或适配词级场景文字编码器，在 RUST 上测试，输出供融合使用的文字区域特征。无文字图像关闭该通道。RUST 识别准确率只作中间指标，不是主验收。", { indent: true }),
  p("内容二：图像外观、场景文字与双语描述的异构融合。分通道编码外观、文字与维/汉文本，采用门控残差融合，对外观—文本与文字—文本分别计算对比损失，检验异构通道是否互相干扰。", { indent: true }),
  p("内容三：跨语言检索与小规模图像理解评价。在 Multi30k-Distant 测试集上报告图像到文本、文本到图像，以及汉查询—维描述、维查询—汉描述的 Recall@K 与 MRR。在测试图像上拟建 200–400 题理解协议。翻译流水线只作对照，不把 BLEU 当主指标。CUTE 与 MC² 仅用于文本编码器继续预训练。", { indent: true }),
  p("预期目标：（1）去掉文字通道后跨语言检索 Recall@5 出现可观测下降；（2）完整模型的汉↔维互检索高于无文字通道与 OCR—翻译流水线；（3）完成小规模理解协议并报告准确率，不将其表述为已有大规模维语 VQA 库；（4）形成可支撑 1 篇中科院三区及以上 SCI 的方法与实验，实验室为第一署名单位。", { indent: true }),
  p("关键问题一：场景文字能否成为维语图像理解的稳定第三通道？关键问题二：外观、连写维文与维/汉描述如何融合而不互相干扰？关键问题三：共享图像作为枢纽，能否在缺少大规模维语 VQA 标注时改善汉↔维互检索？相应假设均可被消融或对照证伪。", { indent: true }),
  h2("2. 拟采取的研究方法、技术路线、实验方案"),
  p("记图像为 I，场景文字区域为 {tk}，维/汉描述为 y_ug、y_zh。外观、文字与文本编码器分别给出 v、s、h。融合采用门控残差 z=v+α σ(W[v;s])⊙s，检索打分为余弦相似度，对齐使用分通道 InfoNCE，并以同一图像上的维/汉描述通过 z 对齐作为视觉枢纽约束。主指标为 Recall@K 与 MRR，理解任务报告准确率。", { indent: true }),
  p("技术路线按“编码—融合—评价”推进。对照固定为：多语 CLIP 零样本、无文字通道、OCR—翻译流水线、完整模型。消融固定为：去文字通道、去门控、去文字—文本损失、去枢纽损失。数据划分遵循公开协议：Multi30k-Distant 为 Train 29000 / Val 1014 / Test 1000；SUST 用于文字编码器训练，RUST 按作者划分测试。不从随机初始化训练大型视觉语言模型。", { indent: true }),
  h2("3. 本课题的特色与创新之处"),
  p("创新点一：把维吾尔语场景文字从识别正确率问题改写为跨语言图像理解的第三通道问题，用去掉文字通道后的检索变化验收，而不是只看 OCR 分数。", { indent: true }),
  p("创新点二：在低资源维—汉数据上联合外观、文字与双语描述，用分通道对比学习和视觉枢纽服务检索，并以翻译流水线为对照；若枢纽不优于翻译，则如实降级该模块。", { indent: true }),
  h2("4. 预期的研究进展、可能遇到的问题及解决对策"),
  p("第一年完成数据合规、场景文字编码器与三类基线；第二年完成融合、跨语言检索、理解协议与论文。主要风险：Multi30k 图像许可、RUST 与 Multi30k 的域差、5 万元算力上限、以及劳务费能否按实验室实报实销列支。对策：核验许可后使用合法子集；不把 OCR 准确率解释为检索增益；只训练融合头与轻量适配；劳务费与业务费分列，若实验室不能报销劳务，则在合同阶段把 3.5 万元调整到指南允许科目。", { indent: true }),
  h2("5. 考核指标及成果形式"),
  p("考核指标：Multi30k-Distant 上的跨语言图文检索 Recall@1 / Recall@5 / MRR；去掉场景文字通道的消融；RUST 文字通道可用性；200–400 题理解准确率（辅助）。成果形式：中科院三区及以上 SCI 论文不少于 1 篇；论文由新疆大学与教育部重点实验室共同署名，并以实验室为第一单位，标注开放课题资助。不承诺专利、平台上线或学生数据实验。", { indent: true }),
];

const section4 = [
  h1("四、研究计划"),
  p("研究期限两年，与指南一致。", { indent: true }),
  p("第一年（2027年1月—12月）：完成公开数据合规审查与划分核对；在 SUST 上训练场景文字编码器并在 RUST 上测试；实现无文字通道的图文对比基线与 OCR—翻译流水线；搭建 Recall@K、MRR 与消融记录脚本；提交年度进展报告。阶段目标是确认文字编码器可用，并得到三类基线的可复现分数。", { indent: true }),
  p("第二年（2028年1月—12月）：完成门控融合与视觉枢纽训练；在 Multi30k-Distant 上报告单语与跨语言检索；完成 200–400 题理解协议与核对；撰写并投稿 SCI 论文；按实验室要求提交结题报告。立项后首期使用 50% 经费，中期报告优或良后再使用其余 50%。", { indent: true }),
];

const section5 = [
  h1("五、研究基础"),
  h2("1. 已具备的实验条件，尚缺少的实验条件和拟解决的途径"),
  p("已具备：新疆大学 GPU 训练环境、深度学习工具链、视觉问答与检索训练流程；SUST/RUST、Multi30k-Distant、CUTE 与 MC² 均为公开数据。", { indent: true }),
  p("尚缺：现成的维语场景文字与图文融合代码；Multi30k-Distant 图像与文本的本地对齐副本；理解协议题面；实验室报销与署名流程需在合同中落实。", { indent: true }),
  p("途径：在开源 CLIP/STR 实现上适配融合头；按许可获取图像，不能合法使用的样本剔除并说明；理解题由研究生编写、申请人抽检。经费按申请人确定为劳务费 3.5 万元、业务费 1.5 万元，实验室实报实销。", { indent: true }),
  h2("2. 申请者和课题组主要成员近期相关成果"),
  p("（1）在国内外核心学术期刊正式发表的科研论文（按与本课题相关性排序）"),
  p("[1] Feng Yan, Zhe Li, Wushour Silamu, Yanbing Li. Knowledge-Aware Image Understanding with Multi-Level Visual Representation Enhancement for Visual Question Answering. Machine Learning, 2024, 113(6): 3789–3805. 第一作者。"),
  p("[2] Feng Yan, Wushour Silamu, Yanbin Li, Yachuang Chai. SPCA-Net: a based on spatial position relationship co-attention network for visual question answering. The Visual Computer, 2022, 38: 3097–3108. 第一作者。"),
  p("[3] Pengfei Xu, Feng Yan*, Yuqing Zhou, Yuancheng Liu, Chuanrui Wu. RSHR+: Progressive question-conditioned visual calibration and structured state-space reasoning for remote sensing visual question answering. Expert Systems with Applications, 2026: 132953. 通讯作者。"),
  p("[4] Pengfei Xu, Feng Yan*. RSSR: Efficient knowledge transfer and deep spatial modeling for remote sensing visual question answering. Computer Vision and Image Understanding, 2026: 104753. 通讯作者。"),
  p("[5] Lihan Tang, Liejun Wang, Gang Wang, Mengyuan Sun, Feng Yan*. Feature Fusion Mamba Hashing via Decoupling for Cross-Modal Retrieval. IEEE Signal Processing Letters, 2026. 通讯作者。"),
  p("[6] Qihui Sun, Feng Yan*, Wanqing Sun, Yuqing Zhou. DWT-Former: Fusing wavelet-based multi-scale features and transformer-based temporal representations for photovoltaic power forecasting. Energy, 2025: 139283. 通讯作者（方法训练经验，非本课题对象）。"),
  p("（2）出版论著情况：无。"),
  p("（3）重要学术会议论文：ICASSP 2026 视觉问答与跨模态检索相关论文 3 篇（Wang & Yan；Xu et al.；Tang et al.）。"),
  p("（4）发明专利：无（不编造）。"),
  p("（5）完成或正在承担的科研项目"),
  p("[1] 多模态融合技术研究及其在新疆产业集群中的应用；自治区天池英才引进计划（青年博士人才）；50万元；2025.02–2028.02；课题负责人。与本课题对象不同，不构成相同内容重复申报。"),
  p("[2] 融合多源数据大模型驱动的光伏发电功率预测方法研究；自治区高校基本科研业务费（培育类）；编号 XJEDU2026P005；2026.01–2026.12；课题负责人。"),
  p("[3] 面向通用领域的多模态视觉问答关键技术研究；自治区优秀博士后资助；3万元；2024.07–2025.11；课题负责人。"),
  p("[4] 面向政企数字化应用的智能知识库与问答系统研发；横向课题；编号 202604140013；12万元；2026.06–2026.10；课题负责人。"),
  p("（6）获奖情况：未在现有材料中列出，不编造。"),
  p("（7）曾经承担的本实验室开放课题：无。"),
];

const budgetCols = [2800, 1800, CONTENT_W - 4600];
const section6 = [
  h1("六、经费预算"),
  p("申请总额 5.00 万元。按申请人确定：劳务费 3.50 万元，业务费 1.50 万元。业务费对应模板既有科目拆分如下。指南列支范围为测试、会议/差旅、资料与出版等，未单列劳务费；劳务费能否报销以实验室合同和实报实销审定为准。"),
  table(budgetCols, [
    row([
      cell("支出科目", 2800, { bold: true, shade: "F2F2F2" }),
      cell("预算经费（万元）", 1800, { bold: true, shade: "F2F2F2", align: AlignmentType.CENTER }),
      cell("备注（计算依据与说明）", CONTENT_W - 4600, { bold: true, shade: "F2F2F2" }),
    ]),
    row([
      cell("（1）测试费", 2800),
      cell("0.80", 1800, { align: AlignmentType.CENTER }),
      cell("模型训练、检索评测与消融实验的计算测试；属业务费。", CONTENT_W - 4600),
    ]),
    row([
      cell("（2）会议费/差旅费", 2800),
      cell("0.40", 1800, { align: AlignmentType.CENTER }),
      cell("与实验室交流及 1 次国内学术会议；属业务费。", CONTENT_W - 4600),
    ]),
    row([
      cell("（3）出版物/文献/信息费", 2800),
      cell("0.30", 1800, { align: AlignmentType.CENTER }),
      cell("论文出版、文献与资料；属业务费。", CONTENT_W - 4600),
    ]),
    row([
      cell("业务费小计", 2800, { bold: true }),
      cell("1.50", 1800, { bold: true, align: AlignmentType.CENTER }),
      cell("测试费+会议差旅+出版物。", CONTENT_W - 4600),
    ]),
    row([
      cell("（4）劳务费", 2800),
      cell("3.50", 1800, { align: AlignmentType.CENTER }),
      cell("研究生助研等劳务。指南未单列该科目，需实验室确认可否列支。", CONTENT_W - 4600),
    ]),
    row([
      cell("合 计", 2800, { bold: true, shade: "F2F2F2" }),
      cell("5.00", 1800, { bold: true, shade: "F2F2F2", align: AlignmentType.CENTER }),
      cell("一般项目申请额度。立项后首期 50%，中期优/良后其余 50%。", CONTENT_W - 4600),
    ]),
  ]),
];

const section7 = [
  h1("七、申请人的承诺和保证"),
  table([CONTENT_W], [
    row([cell([
      "我保证上述填报内容的真实性。如果获得资助，我与本项目组成员将严格遵守重点实验室的有关规定，切实保证研究工作时间，按计划认真开展研究工作，按时报送有关材料，在受资助的研究成果（包括论文、专著、专利等）中标注重点实验室为作者单位，并注明受重点实验室开放研究课题基金资助。署名格式：中央民族大学“民族语言智能分析与安全治理”教育部重点实验室，北京，100081。",
      "申请者（签字）：____________________",
      "年    月    日",
    ], CONTENT_W)]),
  ]),
  h1("八、申请者所在单位审查意见"),
  table([CONTENT_W], [
    row([cell([
      "申请材料真实。本单位同意申报，并为申请者提供必要的条件，保证从事该项研究的时间。",
      "单位（公章）：",
      "年    月    日",
    ], CONTENT_W)]),
  ]),
  h1("九、重点实验室学术委员会评审意见"),
  table([CONTENT_W], [
    row([cell([
      "综合该课题立项依据、研究方案及进展等情况，实验室学术委员会同意该课题申请 。（予以立项；不予立项）",
      "学术委员会主任（签章）",
      "年    月    日",
    ], CONTENT_W)]),
  ]),
  h1("十、重点实验室主任决定"),
  table([CONTENT_W], [
    row([cell([
      "根据学术委员会的评审决定，同意对该课题 。（是否予以资助及资助金额）",
      "实验室主任（签章）：",
      "年    月    日",
    ], CONTENT_W)]),
  ]),
];

const doc = new Document({
  creator: "颜丰",
  title: "场景文字增强的维吾尔语多模态表征融合与跨语言图像理解",
  description: "中央民族大学“民族语言智能分析与安全治理”教育部重点实验室2026年度开放课题申请书",
  styles: {
    default: {
      document: {
        run: { font: "SimSun", size: 24 },
        paragraph: { spacing: { line: 360 } },
      },
    },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickStyle: true, paragraph: { spacing: { before: 240, after: 160 } }, run: { font: "SimSun", size: 32, bold: true } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickStyle: true, paragraph: { spacing: { before: 200, after: 120 } }, run: { font: "SimSun", size: 28, bold: true } },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: A4_W, height: A4_H },
        margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN },
      },
    },
    headers: {
      default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [font("2026年度开放课题申请书", { size: 18, color: "666666" })] })] }),
    },
    footers: {
      default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [font("第 ", { size: 18 }), new TextRun({ children: [PageNumber.CURRENT], font: "Times New Roman", size: 18 }), font(" 页", { size: 18 })] })] }),
    },
    children: [...cover, ...basicInfo, ...section2, ...section3, ...section4, ...section5, ...section6, ...section7],
  }],
});

const out = "/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_MUC_Lab/docs/2026年开放课题申请-新疆大学-颜丰-副教授.docx";
const JSZip = require("jszip");
Packer.toBuffer(doc).then(async (buf) => {
  const zip = await JSZip.loadAsync(buf);
  let core = await zip.file("docProps/core.xml").async("string");
  core = core.replace(/\.\d+Z/g, "Z");
  zip.file("docProps/core.xml", core);
  const fixed = await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" });
  fs.writeFileSync(out, fixed);
  console.log("wrote", out, fixed.length);
});
