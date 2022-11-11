# Modelos Dinamicos

Crear un entorno virtual

```bash
virtualenv -p python3 <nombre>
```

Activar entorne en máquinas **Windows**

```bash
.\env\Scripts\activate
```
Desactivar un entorno virtual

```bash
deactivate
```

Exportar packages instalados por pip

```bash
pip freeze > requirements.txt
```

Instalar paquetes listados desde una archivo de texto plano

```bash
pip install -r requirements.txt
```