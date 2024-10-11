import json
import os

USER_PATH = os.path.expanduser("~")
GAME_PATH = USER_PATH + '/Library/Application Support/nl.noio.kingdom-two-crowns/Release'

GAME_GLOBAL_FILE = 'global-v35'
print(os.name)

def get_game_path():
    if os.name == 'nt':
        return os.getenv('APPDATA') + '\\nl.noio.kingdom-two-crowns\\Release\\'
    elif os.name == 'posix':
        return os.getenv('HOME') + '/Library/Application Support/nl.noio.kingdom-two-crowns/Release/'
    else:
        return os.getenv('APPDATA') + '\\nl.noio.kingdom-two-crowns\\Release\\'
print(get_game_path())
exit()

# windows
# C:\Users\%USERNAME%\AppData\LocalLow\noio\KingdomTwoCrowns\Release\

# mac
# /Users/[USERNAME]/Library/Application Support/nl.noio.kingdom-two-crowns/Release/*

# linux
# /home/[USERNAME]/.config/unity3d/noio/KingdomTwoCrowns/Release/*

# backup
os.chdir(GAME_PATH)
os.system('cp ' + GAME_GLOBAL_FILE + ' ' + GAME_GLOBAL_FILE + '.bak')

campaignIndex = input('Qual campanha deseja alterar? [0, 1 ou 2]: ')

print('Qual jogador deseja alterar?')
playerNumber = input('1 ou 2: ')

print('Qual aparência deseja usar?')
print('1 - Rei sem barba')
print('2 - Rainha com cabelo longo')
print('3 - Rei com barba')
print('4 - Rainha com cabelo ruivo')
print('5 - Rei com capacete de ferro')
model = input('Digite o número da aparência: ')

PLAYER_APPEARENCE_PROPERTY = 'player' + playerNumber + 'Appearance'

with open(GAME_GLOBAL_FILE, 'r') as file:
    file_data = json.load(file)

campaign = file_data['campaigns'][int(campaignIndex)]

# troca a aparência do jogador selecionado
campaign[PLAYER_APPEARENCE_PROPERTY]['model'] = model

with open(GAME_GLOBAL_FILE, 'w') as file:
    json.dump(file_data, file, separators=(',', ':'))