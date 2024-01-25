from Conexion import *

class CClientes:
 
 def mostrarClientes():
    try:
      conectar = CConexion.ConexionBaseDeDatos()
      cursor = conectar.cursor()
      cursor.execute("select * from usuarios;")

      resultado = cursor.fetchall()
      conectar.commit()
      conectar.close()
      return resultado

    except mysql.connector.Error as error:
      print("Error al mostrar los datos {}".format(error))


 def ingresarClientes(nombres,apellidos,sexo):
    try:
      conectar = CConexion.ConexionBaseDeDatos()
      cursor = conectar.cursor()
      sql = "insert into usuarios values(null,%s,%s,%s);"
      # La variable valores  tiene que ser una tupla
      # Como minima expresión es: (valor,) la coma hace que sea una tupla
      # Las tuplas son listas inmutables, eso quiere decir que no se puede modificar
      valores = (nombres,apellidos,sexo)
      cursor.execute(sql,valores)
      conectar.commit()
      print(cursor.rowcount,"Registro ingresado")
      conectar.close()

      
    except mysql.connector.Error as error:
      print("Error de ingreso de datos {}".format(error))

 def modificarClientes(id,nombres,apellidos,sexo):
    try:
      conectar = CConexion.ConexionBaseDeDatos()
      cursor = conectar.cursor()
      sql = "UPDATE usuarios SET usuarios.nombres = %s, usuarios.apellidos = %s, usuarios.sexo = %s WHERE usuarios.id = %s"
      valores = (nombres,apellidos,sexo,id)
      cursor.execute(sql,valores)
      conectar.commit()
      print(cursor.rowcount,"Registro actualizado")
      conectar.close()

      
    except mysql.connector.Error as error:
      print("Error al actualizar los datos {}".format(error))


 def eliminarClientes(id):
    try:
      conectar = CConexion.ConexionBaseDeDatos()
      cursor = conectar.cursor()
      sql = "DELETE FROM usuarios WHERE usuarios.id = %s;"
      valores = (id,)
      cursor.execute(sql,valores)
      conectar.commit()
      print(cursor.rowcount,"Registro eliminado")
      conectar.close()

      
    except mysql.connector.Error as error:
      print("Error al eliminar registro {}".format(error))