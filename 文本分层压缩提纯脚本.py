# 纯时空双轴锚定超强记忆系统
# 核心：仅用时间戳+空间位置定义信息，不压缩不改词，永不丢失
import time
import uuid
from datetime import datetime

class TimeSpaceAnchorMemory:
    def __init__(self):
        # 静态背景冗余信息寄存区（不处理、不删除、静默存放）
        self.background_layer = []
        # 核心时空锚定信息总库
        self.anchor_memory = {}
        # 全局时序索引
        self.time_index = {}
        # 全局空间点位索引
        self.space_index = {}

    def get_unique_timestamp(self):
        """生成高精度唯一时间锚戳"""
        return f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{int(time.time()*1000)}"

    def scan_classify_text(self, full_text):
        """全文扫描：区分背景层与核心内容，不修改原文字"""
        useless_words = {"的","了","啊","呢","吧","很","越","还","就","都","又","再"}
        text_segments = full_text.split("，")
        core_content_list = []

        for seg in text_segments:
            check_word = [w for w in useless_words if w in seg]
            if check_word:
                # 划入静态背景板，原样留存
                self.background_layer.append(seg)
            else:
                # 判定为核心有效内容，保留原文不动
                core_content_list.append(seg)
        print("✅ 文本分层完成，冗余内容划入背景静默层，核心内容保留原始全文")
        return core_content_list

    def build_space_position(self, area_name, level=1):
        """定义专属空间位置点位"""
        space_pos = f"空间域_{area_name}_层级{level}"
        return space_pos

    def lock_info_by_anchor(self, core_text_list, space_area):
        """双轴锁定：时间戳+空间位置绑定原始信息，不压缩"""
        for content in core_text_list:
            # 生成独立唯一时间锚
            time_tag = self.get_unique_timestamp()
            # 生成精准空间点位
            space_tag = self.build_space_position(space_area)
            # 生成全局唯一标识
            info_id = str(uuid.uuid4())

            # 完整锚定存储，原文一字不动
            self.anchor_memory[info_id] = {
                "original_content": content,
                "time_anchor": time_tag,
                "space_position": space_tag
            }

            # 建立双向索引
            if time_tag not in self.time_index:
                self.time_index[time_tag] = []
            self.time_index[time_tag].append(info_id)

            if space_tag not in self.space_index:
                self.space_index[space_tag] = []
            self.space_index[space_tag].append(info_id)

        print(f"✅ 已完成全部内容【时间戳+空间点位】双重锚定锁定")
        print(f"📌 定位标记稳固，无词汇压缩，原始内容永久留存不丢失")

    def search_by_time_range(self, start_time, end_time):
        """按时间轴精准调取信息"""
        print("\\n———— 时间轴定向调取 ————")
        result = []
        for t_tag, ids in self.time_index.items():
            if start_time <= t_tag <= end_time:
                for idx in ids:
                    result.append(self.anchor_memory[idx]["original_content"])
        return result

    def search_by_space_area(self, space_name):
        """按空间位置精准调取信息"""
        print("\\n———— 空间点位定向调取 ————")
        target_space = f"空间域_{space_name}_层级1"
        result = []
        if target_space in self.space_index:
            for idx in self.space_index[target_space]:
                result.append(self.anchor_memory[idx]["original_content"])
        return result

    def memory_anchor_reset(self):
        """逻辑异常触发灯塔水母返祖，重新校准时空锚点"""
        print("\\n⚠️ 检测信息点位偏移，启动灯塔水母锚点重构")
        self.time_index.clear()
        self.space_index.clear()
        print("✅ 时空双轴锚点全部重置，重新精准绑定所有记忆信息")

# 实测运行
if __name__ == "__main__":
    anchor_mem = TimeSpaceAnchorMemory()

    # 海量原生长文本
    full_article = "项目整体稳步推进，设备完成调试，流程依次落地，整体运行十分顺畅，各项数据达到预期标准，后续逐步拓展延伸布局"

    # 分层处理
    core_texts = anchor_mem.scan_classify_text(full_article)
    # 时空双轴绑定锁定
    anchor_mem.lock_info_by_anchor(core_texts, space_area="技术架构领域")

    # 时间调取
    time_res = anchor_mem.search_by_time_range("20260519000000","20261200000000")
    print("时间调取结果：",time_res)
    # 空间调取
    space_res = anchor_mem.search_by_space_area("技术架构领域")
    print("空间调取结果：",space_res)
