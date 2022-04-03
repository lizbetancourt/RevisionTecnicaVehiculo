  

 from flask import Flask, jsofiny,request
 from Conf.ConfBd import mySQLdb
 from flask_restful import Resource




class Tipo_Revision (Resource):

    def Get(self,id): 

        response = {
         'message': 'success',
         'datos':''}
    
        cursor = mySQLdb.connection.cursor()
        query="SELECT ID,NOMBRE_TIPO FROM TIPO_REVISION WHERE ID=%s"
        cursor.execute(query,id)
        tipo=mySQLdb.fetchall()
        mySQLdb.connection.commit()
        cursor.close()

        if len(tipo)>0:
           response['datos']=tipo
        else:
           response['message']="none"
        return jsonify(response)




    def Post(self):
      
      try:
        cursor = mySQLdb.connection.cursor()
        query="INSERT INTO TIPO_REVISION (NOMBRE_TIPO) VALUES (%s)"
        cursor.execute(query,(
               request.json['TipoNombre']
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
    
        revi= self.get(id)['data'][0]

        if revi=="None":
          response = {
         'message': 'No existe Tipo de Revision',
         'status':'False'}
          return jsonify(response)

        if(revi['TipoNombre'] != request.json['TipoNombre']):
          revi['TipoNombre']=request.json['TipoNombre']



        try:
           cursor = mySQLdb.connection.cursor()
           query="UPDATE TIPO_REVISION SET NOMBRE_TIPO=%s"
           cursor.execute(query,(
               request.json['TipoNombre'],
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
      
      inspe= self.get(id)['data'][0]

      if inspe=="None":
          response = {
         'message': 'No existe Tipo Revision',
         'status':'False'}
          return jsonify(response)

      try:
        cursor = mySQLdb.connection.cursor()
        query="DELETE FROM TIPO_REVISION WHERE ID=%s"
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
      


    
    
    
    
    
    
