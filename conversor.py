import ast

def python_para_plantuml(codigo_python):
    """
    Converte código Python em código PlantUML.
    """
    arvore = ast.parse(codigo_python)

    classes = []
    herancas = []

    for no in arvore.body:
        if isinstance(no, ast.ClassDef):
            nome_classe = no.name
            atributos = set()
            metodos = []

            # Verifica herança
            for base in no.bases:
                if isinstance(base, ast.Name):
                    herancas.append((base.id, nome_classe))

            # Procura métodos e atributos
            for item in no.body:
                if isinstance(item, ast.FunctionDef):
                    metodos.append(item.name)

                    for sub_no in ast.walk(item):
                        if (
                            isinstance(sub_no, ast.Attribute)
                            and isinstance(sub_no.value, ast.Name)
                            and sub_no.value.id == "self"
                        ):
                            atributos.add(sub_no.attr)

            classes.append({
                "nome": nome_classe,
                "atributos": sorted(atributos),
                "metodos": metodos
            })

    linhas = []
    linhas.append("@startuml")
    linhas.append("")
    linhas.append("title Diagrama UML de Animais")
    linhas.append("")

    # Cria as classes
    for classe in classes:
        linhas.append(f"class {classe['nome']} {{")

        for atributo in classe["atributos"]:
            linhas.append(f"    - {atributo}")

        if classe["atributos"] and classe["metodos"]:
            linhas.append("")

        for metodo in classe["metodos"]:
            linhas.append(f"    + {metodo}()")

        linhas.append("}")
        linhas.append("")

    # Cria heranças
    for classe_pai, classe_filha in herancas:
        linhas.append(f"{classe_pai} <|-- {classe_filha}")

    linhas.append("")
    linhas.append("@enduml")

    return "\n".join(linhas)


def gerar_arquivo_puml(nome_arquivo, codigo_python):
    """
    Gera um arquivo .puml
    """
    codigo_uml = python_para_plantuml(codigo_python)

    print("=== Código PlantUML gerado ===")
    print(codigo_uml)

    nome_completo = f"{nome_arquivo}.puml"

    with open(nome_completo, "w", encoding="utf-8") as arquivo:
        arquivo.write(codigo_uml)

    print(f"\nArquivo '{nome_completo}' salvo com sucesso!")


# ==========================================
# EXEMPLO DE CLASSES
# ==========================================

meu_codigo_python = """
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def latir(self):
        print("Au au")
"""


# Gera o arquivo UML
gerar_arquivo_puml("diagrama_animais", meu_codigo_python)