import pygame
import time
from bfs import BfsSolver
from dfs import DfsSolver
from ids import IdsSolver

pygame.init()

WindowSize = 300
TileSize = WindowSize // 3
Window = pygame.display.set_mode((WindowSize, WindowSize))
pygame.display.set_caption("8-Puzzle Solver Visualization")

WHITE = (255, 255, 255)

def DrawPuzzle(State, Color):
    Window.fill(WHITE)
    for I in range(9):
        Row, Col = divmod(I, 3)
        TileValue = State[I]
        if TileValue != 0:
            pygame.draw.rect(Window, Color, (Col * TileSize, Row * TileSize, TileSize, TileSize))
            Font = pygame.font.Font(None, 74)
            Text = Font.render(str(TileValue), True, WHITE)
            Window.blit(Text, (Col * TileSize + TileSize // 3, Row * TileSize + TileSize // 4))
    pygame.display.flip()

def VisualizeAndPrintResults(AlgorithmName, Solution, StatesExplored, Color):
    if Solution:
        VisualizeSolutionpygame(Solution, Color) 
        DisplaySolvedMessage(len(Solution), AlgorithmName, Color)
    print(f"{AlgorithmName}: {StatesExplored} states explored, solution steps: {len(Solution)}")

def VisualizeSolutionpygame(Solution, Color):
    for State in Solution:
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                pygame.quit()
        DrawPuzzle(State, Color) 
        time.sleep(1)  

def DisplaySolvedMessage(Steps, AlgorithmName, Color):
    Font = pygame.font.Font(None, 24)
    Text = Font.render(f"Solved! {AlgorithmName} took {Steps} steps.", True, (255, 255, 255))
    
    TextWidth, TextHeight = Text.get_size()
    
    XPosition = (WindowSize - TextWidth) // 2
    YPosition = (WindowSize - TextHeight) // 2

    Window.fill(Color)
    
    Window.blit(Text, (XPosition, YPosition))
    pygame.display.flip()
    
    time.sleep(2)


def Main():
    InitialState = [1, 2, 4, 3, 5, 6, 0, 8, 7]
    GoalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    SolutionBfs, StatesBfs = BfsSolver(InitialState, GoalState)
    SolutionDfs, StatesDfs = DfsSolver(InitialState, GoalState)
    SolutionIds, StatesIds = IdsSolver(InitialState, GoalState)

    VisualizeAndPrintResults("BFS", [InitialState] + SolutionBfs, StatesBfs, (100, 149, 237))  # Blue
    VisualizeAndPrintResults("DFS", [InitialState] + SolutionDfs, StatesDfs, (110, 149, 108))  # Green
    VisualizeAndPrintResults("IDS", [InitialState] + SolutionIds, StatesIds, (255, 153, 28))  # Yellow

    pygame.quit()

if __name__ == '__main__':
    Main()
