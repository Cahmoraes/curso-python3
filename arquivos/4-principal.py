from agenda import add_contact, view_contacts, delete_contacts


def main():
    while True:
        print("\nAgenda de Contatos")
        print("1. Adiciona Contato")
        print("2. Lista Contato")
        print("3. Remover Contatos")
        print("4. Sair")
        choice = int(input("Escolha a opção (1 - 4)\n"))
        match choice:
            case 1:
                add_contact()
            case 2:
                view_contacts()
            case 3:
                delete_contacts()
            case 4:
                break
            case _:
                print("Informe uma opção válida!")


if __name__ == "__main__":
    main()
