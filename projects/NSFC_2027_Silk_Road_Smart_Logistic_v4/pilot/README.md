# 最小先导实验证据包

## 当前状态

- 方案、配置、字段规范与空白模板：已建立。
- 原始数据、网络回放日志、模型结果与结论：尚无。
- 真实 2G/3G 轨迹、代表性板卡、物理功耗、现场或货物级配对：尚未提供。

因此，本目录目前是“可执行骨架”，不能作为已完成预实验的证明。

## 目录

- config：实验矩阵与弱网压力档位。
- schema：三时钟数据字典与事件定义。
- templates：单次运行、数据说明、证据清单和结果登记模板。
- checklists：运行前检查与证据验收。
- evidence：后续按 raw、processed、logs、results、reports 保存证据；原始层只读。

## 执行顺序

1. 复制 templates/run_manifest.yaml 到 evidence/logs/<run_id>/run_manifest.yaml。
2. 填写设备、软件、时钟、场景、网络配置、随机种子、伦理/隐私和责任人信息。
3. 填写 templates/preregistration.md，签署并计算 SHA-256 后冻结。
4. 按 checklists/preflight.md 完成干运行。
5. 原始载荷写入 evidence/raw/<run_id>/，不得覆盖；派生数据写入 processed。
6. 将配置、网络状态、缓存、重传、资源和标准输出日志写入 logs/<run_id>/。
7. 对每个文件计算 SHA-256，并逐项登记到 evidence_manifest.csv 的工作副本。
8. 先完成开发与校准，再封存锁定评估标签；同一 entity_id 的全部副本只能进入一个集合。
9. 结果写入 result_registry.csv 的工作副本，报告使用 experiment_report.md。
10. 按 evidence_acceptance.md 审核；未通过项不得回写标书。

## 命名约定

- run_id：PILOT-YYYYMMDD-场景-四位序号。
- evidence_id：EV-类型-YYYYMMDD-四位序号。
- network_profile_id：W0–W4 为参数化压力；T-* 为有来源轨迹；F-* 为现场实测。
- method_id：B0/B1/B2 为 C1 基线或消融；FIFO/EDF/PAV 为 C2 基线；M1/M2 为候选方法。

## 状态枚举

- placeholder：仅为模板占位。
- planned：配置已确定但未运行。
- captured：已采集，尚未核验。
- verified：哈希、字段和来源已核验。
- analyzed：已按冻结计划分析。
- accepted：通过证据验收，可用于相应层级表述。
- rejected：证据链不完整或偏离预注册，不用于主张。

## 硬约束

- 不覆盖原始文件，不以清洗后数据代替原始证据。
- 不把 W0–W4 写成真实 2G/3G 轨迹。
- 不把电子封志代理写成电子封志实测。
- 不把窗口或网络副本当作独立实体。
- 不使用锁定评估标签选择模型、阈值或截止期。
- 没有物理功耗测量时，功耗来源必须写 estimated 或 not_available。
- 每个数字必须能由 result_id → evidence_id → 文件路径与 SHA-256 反向追溯。

正式方案见 [docs/06_最小先导实验执行方案.md](../docs/06_最小先导实验执行方案.md)。
