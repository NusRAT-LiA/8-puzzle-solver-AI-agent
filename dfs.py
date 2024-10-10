import pygame
from bfs import MoveTile


def DfsSolver(InitialState, GoalState, DepthLimit=50):
    Stack = [(InitialState, [])]
    Visited = set()
    Visited.add(tuple(InitialState))
    StatesExplored = 0

    while Stack:
        CurrentState, Path = Stack.pop()
        StatesExplored += 1

        if CurrentState == GoalState:
            return Path, StatesExplored

        if len(Path) >= DepthLimit:
            continue

        for Direction in ['up', 'down', 'left', 'right']:
            NewState = MoveTile(CurrentState, Direction)
            if NewState and tuple(NewState) not in Visited:
                Visited.add(tuple(NewState))
                Stack.append((NewState, Path + [NewState]))

    return None, StatesExplored
