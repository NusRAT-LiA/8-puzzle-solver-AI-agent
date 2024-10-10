from bfs import MoveTile


def IdsSolver(InitialState, GoalState):
    def Dls(State, Path, Depth, Visited):
        nonlocal StatesExplored
        StatesExplored += 1

        if State == GoalState:
            return Path

        if Depth == 0:
            return None

        for Direction in ['up', 'down', 'left', 'right']:
            NewState = MoveTile(State, Direction)
            if NewState and tuple(NewState) not in Visited:
                Visited.add(tuple(NewState))
                Result = Dls(NewState, Path + [NewState], Depth - 1, Visited)
                if Result:
                    return Result
        return None

    Depth = 0
    StatesExplored = 0
    while True:
        Visited = set()
        Visited.add(tuple(InitialState))
        Result = Dls(InitialState, [], Depth, Visited)
        if Result:
            return Result, StatesExplored
        Depth += 1
