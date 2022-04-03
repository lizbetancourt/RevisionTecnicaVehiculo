  

 from flask import Flask, jsofiny,request
 from Conf.ConfBd import mySQLdb
 from flask_restful import Resource




class vehiculo (Resource):

    def Get(self,id): 

        response = {
         'message': 'success',
         'datos':''}
    
        cursor = mySQLdb.connection.cursor()
        query="SELECT ID,MARCA,MODELO,PATENTE,AÑO,PERSONA_ID FROM VEHICULO WHERE ID=%s"
        cursor.execute(query,id)
        vehi=mySQLdb.fetchall()
        mySQLdb.connection.commit()
        cursor.close()

        if len(vehi)>0:
           response['datos']=vehi
        else:
           response['message']="none"
        return jsonify(response)




    def Post(self):
      
      try:
        cursor = mySQLdb.connection.cursor()
        query="INSERT INTO VEHICULO (ID,MARCA,MODELO,PATENTE,AÑO,PERSONA_ID) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(
               request.json['marca'],
               request.json['modelo'],
               request.json['patente'],
               request.json['año'],
               request.json['idPersona']

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
    
        vehi= self.get(id)['data'][0]

        if vehi=="None":
          response = {
         'message': 'No existe vehiculo',
         'status':'False'}
          return jsonify(response)

        if(vehi['marca'] != request.json['marca']):
          vehi['marca']=request.json['marca']

        if(vehi['modelo'] != request.json['modelo']):
          vehi['modelo']=request.json['modelo']
        
        if(vehi['patente'] != request.json['patente']):
          vehi['patente']=request.json['patente']

        if(vehi['año'] != request.json['año']):
          vehi['año']=request.json['año']

        if(vehi['idPersona'] != request.json['idPersona']):
          vehi['idPersona']=request.json['idPersona']
        

        try:
           cursor = mySQLdb.connection.cursor()
           query="UPDATE VEHICULO SET MARCA=%s,MODELO=%s,PATENTE=%s,AÑO=%s,PERSONA_ID=%s WHERE ID=%s"
           cursor.execute(query,(
               request.json['marca'],
               request.json['modelo'],
               request.json['patente'],
               request.json['año'],
               request.json['idPersona'],
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
      
      vehi= self.get(id)['data'][0]

      if vehi=="None":
          response = {
         'message': 'No existe Vehiculo',
         'status':'False'}
          return jsonify(response)

      try:
        cursor = mySQLdb.connection.cursor()
        query="DELETE FROM VEHICULO WHERE ID=%s"
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
      


    
    
    
    
    
    
