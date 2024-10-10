from collections import deque


Moves = {
    'up': -3,
    'down': 3,
    'left': -1,
    'right': 1
}

def FindBlank(State):
    return State.index(0)

def MoveTile(State, Direction):
    BlankIndex = FindBlank(State)
    TargetIndex = BlankIndex + Moves[Direction]

    if Direction == 'left' and BlankIndex % 3 == 0:
        return None
    if Direction == 'right' and BlankIndex % 3 == 2:
        return None
    if TargetIndex < 0 or TargetIndex >= 9:
        return None

    NewState = list(State)
    NewState[BlankIndex], NewState[TargetIndex] = NewState[TargetIndex], NewState[BlankIndex]
    return NewState

def BfsSolver(InitialState, GoalState):
    Queue = deque([(InitialState, [])])
    Visited = set()
    Visited.add(tuple(InitialState))
    StatesExplored = 0

    while Queue:
        CurrentState, Path = Queue.popleft()
        StatesExplored += 1

        if CurrentState == GoalState:
            return Path, StatesExplored

        for Direction in ['up', 'down', 'left', 'right']:
            NewState = MoveTile(CurrentState, Direction)
            if NewState and tuple(NewState) not in Visited:
                Visited.add(tuple(NewState))
                Queue.append((NewState, Path + [NewState]))

    return None, StatesExplored
