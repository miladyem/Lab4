from sokoban_model import MoveResponse, SokobanModel
from sokoban_view import SokobanView

class SokobanController:
    def __init__(self, xsb_file):
        with open(xsb_file, "r") as f:
            self.model = SokobanModel(list(f))
        self.view = SokobanView()

    def game_loop(self):
        move_response = MoveResponse.VALID
        while True:
            if move_response == MoveResponse.VALID:
                self.view.print(self.model)
            else:
                print(move_response.value)

            player_movement = input("Enter move (z, q, w, s) or 'r' to reset, 'c' to quit: ").strip()

            # Commandes pour les mouvements
            if player_movement == 'z':
                move_response = self.model.move(0, -1)
            elif player_movement == 'q':
                move_response = self.model.move(-1, 0)
            elif player_movement == 'w':
                move_response = self.model.move(0, 1)
            elif player_movement == 's':
                move_response = self.model.move(1, 0)
            # Commande pour réinitialiser le niveau
            elif player_movement == 'r':
                print("Réinitialisation du niveau...")
                self.model.reset_level(self.model.initial_data)  # Réinitialise le niveau
            # Commande pour quitter le jeu
            elif player_movement == 'c':
                print("Quitter le jeu.")
                break  # Quitter la boucle de jeu et ainsi le programme
            else:
                print("Commande invalide. Veuillez entrer une commande valide.")


# class SokobanController:
#     def __init__(self, xsb_file):
#         with open(xsb_file, "r") as f:
#             self.model = SokobanModel(list(f))
#         self.view = SokobanView()

#     def game_loop(self):
#         move_response = MoveResponse.VALID
#         while True:
#             if move_response == MoveResponse.VALID:
#                 self.view.print(self.model)
#             else:
#                 print(move_response.value)
#             player_movement = input("Enter move (z, q, w, s) or 'r' to reset, 'c' to quit: ").strip()
#             match player_movement:
#                 case 'z':
#                     move_response = self.model.move(0, -1)
#                 case 'q':
#                     move_response = self.model.move(-1, 0)
#                 case 'w':
#                     move_response = self.model.move(0, 1)
#                 case 's':
#                     move_response = self.model.move(1, 0)

