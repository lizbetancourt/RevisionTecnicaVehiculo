  

 from flask import Flask, jsofiny,request
 from Conf.ConfBd import mySQLdb
 from flask_restful import Resource




class Inspeccion (Resource):

    def Get(self,id): 

        response = {
         'message': 'success',
         'datos':''}
    
        cursor = mySQLdb.connection.cursor()
        query="SELECT ID,REVISION_ID,TIPO_INSPECCION, OBSERVACIONES,ESTADO,PERSONA_ID FROM INSPECCION WHERE ID=%s"
        cursor.execute(query,id)
        inspe=mySQLdb.fetchall()
        mySQLdb.connection.commit()
        cursor.close()

        if len(inspe)>0:
           response['datos']=inspe
        else:
           response['message']="none"
        return jsonify(response)




    def Post(self):
      
      try:
        cursor = mySQLdb.connection.cursor()
        query="INSERT INTO INSPECCION (ID,REVISION_ID,TIPO_INSPECCION, OBSERVACIONES,ESTADO,PERSONA_ID) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(
               request.json['idRevision'],
               request.json['tipoInspeccion'],
               request.json['Observaciones'],
               request.json['estado'],
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
    
        inspe= self.get(id)['data'][0]

        if inspe=="None":
          response = {
         'message': 'No existe Inspeccion',
         'status':'False'}
          return jsonify(response)

        if(inspe['idRevision'] != request.json['idRevision']):
          inspe['idRevision']=request.json['idRevision']

        if(inspe['tipoInspeccion'] != request.json['tipoInspeccion']):
          inspe['tipoInspeccion']=request.json['tipoInspeccion']
        
        if(inspe['Observaciones'] != request.json['Observaciones']):
          inspe['Observaciones']=request.json['Observaciones']

        if(inspe['estado'] != request.json['estado']):
          inspe['estado']=request.json['estado']

        if(inspe['idPersona'] != request.json['idPersona']):
          inspe['idPersona']=request.json['idPersona']
        

        try:
           cursor = mySQLdb.connection.cursor()
           query="UPDATE INSPECCION SET REVISION_ID=%s,REVISION_ID=%s,TIPO_INSPECCION=%s, OBSERVACIONES=%s,ESTADO=%s,PERSONA_ID=%s WHERE ID=%s"
           cursor.execute(query,(
               request.json['idRevision'],
               request.json['tipoInspeccion'],
               request.json['Observaciones'],
               request.json['estado'],
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
      
      inspe= self.get(id)['data'][0]

      if inspe=="None":
          response = {
         'message': 'No existe Inspeccion',
         'status':'False'}
          return jsonify(response)

      try:
        cursor = mySQLdb.connection.cursor()
        query="DELETE FROM INSPECCION WHERE ID=%s"
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
      


    
    
    
    
    
    
