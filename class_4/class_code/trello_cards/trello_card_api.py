from trello import TrelloClient, Board
import os

class TrelloHelper:
    client: TrelloClient = None
    board: Board = None

    def __init__(self):
        super().__init__()
        self.client = TrelloClient(
            api_key=os.getenv('TRELLO_API_KEY'),
            token=os.getenv('TRELLO_TOKEN')
        )
        self.board = self.client.get_board(os.getenv('TRELLO_BOARD_ID'))

        # Create a label for AI generated cards if it doesn't exist
        ai_label = "AI gen"
        ai_gen_label = [label for label in self.board.get_labels() if label.name.lower() == ai_label.lower()]
        if not ai_gen_label:
            ai_gen_label = self.board.add_label("AI gen", "blue")

    def create_card(self, name: str, description: str, labels: list[str] = []) -> str:
        default_list = self.board.list_lists()[0]  # You might want to specify a particular list
        
        labels.append("AI gen")
        trello_labels = [label for label in self.board.get_labels() if label.name.lower() in [lbl.lower() for lbl in labels]]

        card = default_list.add_card(name=name, desc=description, labels=trello_labels)
        return card