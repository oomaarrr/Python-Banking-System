import time,subprocess,os

current_user = None
database_logins = {}
balance = 0
currencies = {
    'USD': ('Dólar estadounidense', '$'),
    'EUR': ('Euro', '€'),
    'JPY': ('Yen japonés', '¥'),
    'GBP': ('Libra esterlina', '£'),
    'AUD': ('Dólar australiano', '$'),
    'CAD': ('Dólar canadiense', '$'),
    'CHF': ('Franco suizo', 'CHF'),
    'CNY': ('Renminbi chino', '¥'),
    'HKD': ('Dólar de Hong Kong', '$'),
    'NZD': ('Dólar neozelandés', '$'),
    'SEK': ('Corona sueca', 'kr'),
    'KRW': ('Won surcoreano', '₩'),
    'SGD': ('Dólar de Singapur', '$'),
    'NOK': ('Corona noruega', 'kr'),
    'MXN': ('Peso mexicano', '$')
}
act_currency = currencies[list(currencies.keys())[0]]
print(act_currency)

def clear_screen():
    comando = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(comando, shell=True)

def check_acc():
    clear_screen()
    print(f'CUENTA DE {current_user.upper()}:\n')
    print(f'Balance: {balance}')
    print(f'Divisa: {act_currency[0]} ({act_currency[1]})')
    input('\n\nPresiona ENTER para continuar...')
    
def logout():
    clear_screen()
    current_user = None
    balance = 0
    act_currency = currencies[list(currencies.keys())[0]]
    print('Cuenta cerrada con éxito, vuelva pronto')
    time.sleep(2)
    exit()

def typing_error(bad_input):
    print(f"'{bad_input}' no es un comando existente")
    time.sleep(2)

def mod_balance(sign):
    global balance
    clear_screen()
    if sign:
        amount = int(input('¿Cuanto dinero quiere depositar? '))
        balance+= amount
        print(f'Depósito realizado con éxito, balance actual: {balance}{act_currency[1]}')
        time.sleep(2)
    else:
        while True:
            amount = int(input('¿Cuanto dinero quiere retirar? '))
            if amount <= balance:
                balance-=amount
                print(f'Retirada realizada con éxito, balance actual: {balance}{act_currency[1]}')
                time.sleep(2)
                break
            else:
                print(f'Error: Fondos insuficientes. Balance de la cuenta: {balance}{act_currency[1]}')
                time.sleep(2)
def change_currency():
    global act_currency
    print(f'Divisa actual: {act_currency[0]}')
    while True:
        clear_screen()
        print('Divisas disponibles:')
        for i in range (len(currencies)):
            print(f'{i+1}.{list(currencies.keys())[i]} ({list(currencies.values())[i][0]})')
        cambio = int(input('Introduzca el numero de la divisa deseada: '))-1
        try:
            act_currency = currencies[list(currencies.keys())[cambio]]
            print(f'Divisa cambiada a {act_currency[0]} ({act_currency[1]}) correctamente')
            time.sleep(2)
            break
        except:
            typing_error(cambio+1)

def menu_acc():
    while True:
        log_sign = input("¿Tiene una cuenta? [s/n]: ").lower()
        if log_sign == 's':
            login()
            break
        elif log_sign == 'n':
            signup()
            break
        else:
            typing_error(log_sign)

def signup():
    global current_user
    clear_screen()
    user = input("\nIntroduzca un nuevo nombre de usuario: ")
    password = input("Introduzca una contraseña: ")
    database_logins[user] = password
    print("Cuenta creada con éxito")
    current_user = user
    time.sleep(2)
    menu()

def login():
    global current_user
    clear_screen()
    user = input("\nIntroduzca su nombre de usuario: ")
    password = input("Introduzca su contraseña: ")
   
    if user in database_logins:
        if database_logins[user] == password:
            current_user = user
            menu()
        else:
            print("Contraseña incorrecta. Inténtelo de nuevo.")
            time.sleep(2)
            login()
    else:
        create = input("\nUsuario no encontrado. ¿Desea crear uno? [s/n]: ").lower()
        if create == 's':
            signup()
        elif create == 'n':
            login()
        else:
            typing_error(create)
            login()
 
def menu():
    while True:
        clear_screen()
        print(f"Bienvenido, {current_user}. Seleccione una de las opciones disponibles:")
        print("1. Comprobar cuenta")
        print("2. Retirar Dinero")
        print("3. Depositar Dinero")
        print("4. Cambiar divisa")
        print("5. Cerrar Sesión")
       
        choose = input("Introduzca el numero de la opción que desee: ")
        match choose:
            case '1':
                check_acc()
            case '2':
                mod_balance(False)
            case '3':
                mod_balance(True)
            case '4':
                change_currency()
            case '5':
                logout()

def main():
    clear_screen()
    print("BANCO DE PYTHON")
    if current_user == None:
        menu_acc()
    else:
        menu()

if __name__ == "__main__":
    main()