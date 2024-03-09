from langgraph.graph import StateGraph as StateGraphOrg
from langchain.load.dump import dumps
import json
import requests
from langchain_core.runnables import Runnable
from langchain_core.runnables.base import (
    RunnableLambda,
    RunnableLike,
    coerce_to_runnable,
)
from langgraph.graph.graph import END, START, CompiledGraph, Graph
from typing import Any, Callable, Dict, NamedTuple, Optional, Sequence

START = "__start__"
END = "__end__"

class StateGraphWork(StateGraphOrg):

    def __init__(self, options,serverUrl = ''):
        super().__init__(options)
        self.logList = []
        self.nodeList = []
        self.edgeList = []
        self.start = ''
        self.end = ''
        # self.serverUrl = options.get('server_url', None)
        self.serverUrl = serverUrl


    # 增加节点
    def add_node(self, key: str, action: RunnableLike) -> None:
        # nodelist中添加node节点的输入输出
        self.nodeList.append({'type': 'node', 'name': key})
        def on_end(run):
            log = {
                'type': 'node',
                'name': key,
                'input': run.inputs,
                'output': run.outputs,
            }
            self.logList.append(log)
        super().add_node(key,coerce_to_runnable(action).with_listeners(on_end=on_end))

    # 增加边
    def add_edge(self, start_key: str, end_key: str) -> None:
        super().add_edge(start_key,end_key)
        self.edgeList.append([start_key, end_key])


    def add_conditional_edges(
        self,
        start_key: str,
        condition: Callable[..., str],
        conditional_edge_mapping: Optional[Dict[str, str]] = None,
    ) -> None:
        self.edgeList.append([start_key, conditional_edge_mapping])
        def wrapper_condition(state):
            # print("wrapper_condition")
            next_state = condition(state)
            if next_state == 'end':
                log = {
                    'nodes': self.nodeList,
                    'edges': self.edgeList,
                    'start': self.start,
                    'end': self.end,
                    'logs': self.logList,
                }
                # Save log to file
                print(dumps(log, sort_keys=True, indent=4, separators=(', ', ': ')))
                # Submit to server
                # if self.serverUrl:
                    # requests.post(self.serverUrl, data=log)
            else:
                self.logList.append({
                    'type': 'ConditionalEdges',
                    'name': start_key,
                    'input': state,
                    'output': next_state,
                })
            return next_state

        super().add_conditional_edges(start_key, wrapper_condition, conditional_edge_mapping)


    def setEntryPoint(self, agent):
        self.start = agent
        super().setEntryPoint(agent)

    def set_entry_point(self, key: str) -> None:
        super().set_entry_point(key)
        self.start = key

    def setFinishPoint(self, agent):
        self.end = agent

    def compile(self):
        return super().compile()

    def returnres(self):
        output = {
            'nodes': self.nodeList,
            'edges': self.edgeList,
            'logs': self.logList,
        }
        return output
