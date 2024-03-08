import os
import pandas as pd
import mpdfg

blasting_event_log_path = os.path.join("data", "blasting_with_rework_event_log.csv")
road_traffic_event_log_path = os.path.join("data", "Road_Traffic_Fine_Management_Process.csv")

blasting_event_log = pd.read_csv(blasting_event_log_path, sep=";")
road_traffic_event_log = pd.read_csv(road_traffic_event_log_path, sep=",")

# Key is the column format name of pm4py
# Value is the column name of the specific log and soon to be changed
# We will always need 3 columns for case, activity and timestamp
blasting_format = {
    "case:concept:name": "Case ID",
    "concept:name": "Activity",
    "time:timestamp": "Complete",
    "start_timestamp": "Start",
    "org:resource": "Resource",
    "cost:total": "Cost",
}

road_traffic_format = {
    "case:concept:name": "Case ID",
    "concept:name": "Activity",
    "time:timestamp": "Complete Timestamp",
    "start_timestamp": "",
    "org:resource": "Resource",
    "cost:total": "",
}

blasting_event_log = mpdfg.log_formatter(blasting_event_log, blasting_format)
road_traffic_event_log = mpdfg.log_formatter(road_traffic_event_log, road_traffic_format)

freq_statistics = ["absolute-activity", "absolute-case", "relative-case", "relative-activity"]
numbers_statistics = ["mean", "min", "max", "stdev", "median", "sum"]

(
    multi_perspective_dfg,
    start_activities,
    end_activities,
) = mpdfg.discover_multi_perspective_dfg(
    log=blasting_event_log,
    calculate_cost=True,
    calculate_frequency=True,
    calculate_time=True,
    frequency_statistic="absolute-activity",
    time_statistic="mean",
    cost_statistic="mean",
)

mpdfg.view_multi_perspective_dfg(
    multi_perspective_dfg=multi_perspective_dfg,
    start_activities=start_activities,
    end_activities=end_activities,
    visualize_frequency=True,
    visualize_cost=True,
    visualize_time=True,
    cost_currency="USD",
    rankdir="TB",
    figsize=(20, 20),
)


breakpoint()

mpdfg.save_vis_multi_perspective_dfg(
    multi_perspective_dfg=multi_perspective_dfg,
    start_activities=start_activities,
    end_activities=end_activities,
    file_name="mpdfg_graph",
    visualize_frequency=True,
    visualize_time=True,
    visualize_cost=True,
    cost_currency="USD",
    format="png",
    rankdir="TD",
    diagram_tool="graphviz",
)

for b1 in [True, False]:
    for b2 in [True, False]:
        for b3 in [True, False]:
            mpdfg.save_vis_multi_perspective_dfg(
                multi_perspective_dfg=multi_perspective_dfg,
                start_activities=start_activities,
                end_activities=end_activities,
                file_name=f'imgs/ex_{"freq_" if b1 else ""}{"time_" if b2 else ""}{"cost" if b3 else ""}',
                visualize_frequency=b1,
                visualize_time=b2,
                visualize_cost=b3,
                format="png",
                rankdir="TD",
                diagram_tool="graphviz",
            )
