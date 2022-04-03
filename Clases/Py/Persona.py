  

 from flask import Flask, jsofiny,request
 from Conf.ConfBd import mySQLdb
 from flask_restful import Resource




class persona (Resource):

    def Get(self,id): 

        response = {
         'message': 'success',
         'datos':''}
    
        cursor = mySQLdb.connection.cursor()
        query="SELECT ID,IDENTIFICADOR,NOMBRE, APELLIDO FROM PERSONA WHERE ID=%s"
        cursor.execute(query,id)
        per=mySQLdb.fetchall()
        mySQLdb.connection.commit()
        cursor.close()

        if len(per)>0:
           response['datos']=per
        else:
           response['message']="none"
        return jsonify(response)




    def Post(self):
      
      try:
        cursor = mySQLdb.connection.cursor()
        query="INSERT INTO PERSONA (IDENTIFICACION,NOMBRE,APELLIDO) VALUES (%s,%s,%s)"
        cursor.execute(query,(
               request.json['identificacion'],
               request.json['nombre'],
               request.json['apellido']

        ))
        mySQLdb.connection.commit()
        cursor.close()   

        response = {
         'message': 'success',
         'status':'True'}

        return jsonify(response)

      except Exception as ex:
         response = {
         'message': 'error',
         'status':'False'}

      return jsonify(response)




    def Update(self,id):
    
        per= self.get(id)['data'][0]

        if per=="None":
          response = {
         'message': 'No existe Persona',
         'status':'False'}
          return jsonify(response)

        if(per['identificacion'] != request.json['identificacion']):
          per['identificacion']=request.json['identificacion']

        if(per['nombre'] != request.json['nombre']):
          per['nombre']=request.json['nombre']
        
        if(per['apellido'] != request.json['apellido']):
          per['apellido']=request.json['apellido']
        

        try:
           cursor = mySQLdb.connection.cursor()
           query="UPDATE PERSONA SET IDENTIFICACION=%s,NOMBRE=%s,APELLIDO=%s WHERE ID=%s"
           cursor.execute(query,(
               per.json['identificacion'],
               per.json['nombre'],
               per.json['apellido'],
               id

           ))
           cursor.close()   

           response = {
           'message': 'Actualizado',
           'status':'True'}

           return jsonify(response)

        except Exception as ex:
          response = {
         'message': 'error actualizando',
         'status':'False'}

          return jsonify(response)



    def Delete(self,id):
      
      per= self.get(id)['data'][0]

      if per=="None":
          response = {
         'message': 'No existe Persona',
         'status':'False'}
          return jsonify(response)

      try:
        cursor = mySQLdb.connection.cursor()
        query="DELETE FROM PERSONA WHERE ID=%s"
        cursor.execute(query,(id ))
        mySQLdb.connection.commit()
        cursor.close()   

        response = {
         'message': 'Eliminado',
         'status':'True'}

        return jsonify(response)

      except Exception as ex:
         response = {
         'message': 'error eliminando',
         'status':'False'}

      return jsonify(response)
      


    
    
    
    
    
    
