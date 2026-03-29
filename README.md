# 💼 Alke Wallet - Sistema Web con Django

Aplicación web desarrollada con Django que permite gestionar usuarios, cuentas y transacciones financieras básicas, utilizando una base de datos relacional y el ORM de Django.

---

## 📌 Descripción del proyecto

Este proyecto corresponde al desarrollo de una aplicación web que implementa operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre un conjunto de entidades relacionadas, integrando:

- Modelos de datos
- Migraciones
- ORM de Django
- Vistas y templates

El sistema simula una billetera digital básica (_wallet_), donde los usuarios pueden tener cuentas y realizar transacciones.

---

## 🧠 Modelo de datos

El sistema está compuesto por tres entidades principales:

### 👤 Usuario

- nombre
- correo
- fecha de registro

### 💳 Cuenta

- pertenece a un usuario
- número de cuenta único
- saldo
- fecha de creación

### 💸 Transacción

- asociada a una cuenta
- tipo (depósito o retiro)
- monto
- fecha
- descripción opcional

---

## 🔗 Relaciones

- Un **usuario** puede tener múltiples **cuentas**
- Una **cuenta** puede tener múltiples **transacciones**

Esto se implementa mediante relaciones `ForeignKey` en Django.

---

## ⚙️ Tecnologías utilizadas

- Python 3.x
- Django
- SQLite
- HTML (templates Django)

---

## 🗄️ Base de datos

Se utiliza **SQLite** como base de datos, configurada por defecto en Django mediante el archivo `settings.py`.

---

## 🔄 Migraciones

Las migraciones permiten mantener sincronizado el esquema de la base de datos con los modelos definidos.

Comandos utilizados:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🔧 Funcionalidades (CRUD)

El sistema permite realizar operaciones completas sobre cada entidad:

### Usuarios

- Crear usuario
- Listar usuarios
- Editar usuario
- Eliminar usuario

### Cuentas

- Crear cuenta asociada a un usuario
- Listar cuentas
- Editar cuenta
- Eliminar cuenta

### Transacciones

- Crear transacción asociada a una cuenta
- Listar transacciones
- Editar transacción
- Eliminar transacción

---

## 🖥️ Interfaz de usuario

Se implementaron vistas utilizando templates de Django que permiten interactuar con el sistema de manera simple y clara.

Incluye:

- Navegación básica
- Formularios para CRUD
- Listados de datos

---

## 🚀 Ejecución del proyecto

### 1. Clonar repositorio

```bash
git clone <url-del-repo>
cd alke_wallet
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno

Windows:

```bash
venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor

```bash
python manage.py runserver
```

### 8. Acceder al sistema

- Aplicación: http://127.0.0.1:8000/
- Panel admin: http://127.0.0.1:8000/admin/

---

## 📸 Evidencia de funcionamiento

El proyecto incluye capturas de pantalla que muestran:

- Creación de usuarios
- Creación de cuentas
- Registro de transacciones
- Listados de datos
- Panel de administración
- Ejecución de migraciones

---

## 📌 Conclusión

Este proyecto demuestra la capacidad de:

- Integrar Django con una base de datos relacional
- Utilizar el ORM para gestionar datos
- Implementar operaciones CRUD completas
- Estructurar una aplicación web funcional con buenas prácticas básicas
