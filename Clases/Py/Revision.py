  

 from flask import Flask, jsofiny,request
 from Conf.ConfBd import mySQLdb
 from flask_restful import Resource




class Revision (Resource):

    def Get(self,id): 

        response = {
         'message': 'success',
         'datos':''}
    
        cursor = mySQLdb.connection.cursor()
        query="SELECT ID,VEHICULO_ID,APROBADO,OBSERVACIONES,PERSONA_ID,FECHA_REVISION FROM REVISION WHERE ID=%s"
        cursor.execute(query,id)
        revi=mySQLdb.fetchall()
        mySQLdb.connection.commit()
        cursor.close()

        if len(revi)>0:
           response['datos']=revi
        else:
           response['message']="none"
        return jsonify(response)


    def historial(self,Patente):

        response = {
         'message': 'success',
         'datos':''}
    
        cursor = mySQLdb.connection.cursor()
        query="SELECT ID,VEHICULO,MODELO,MARCA,APROBADO,OBSERVACIONES,PERSONA_ID,FECHA_REVISION FROM REVISION INNER JOIN VEHICULO ON REVISION.PATENTE=VAHICULO.PATENTE WHERE PATENTE=%s"
        cursor.execute(query,Patente)
        revi=mySQLdb.fetchall()
        mySQLdb.connection.commit()
        cursor.close()

        if len(revi)>0:
           response['datos']=revi
        else:
           response['message']="none"
        return jsonify(response)



    def Post(self):
      
      try:
        cursor = mySQLdb.connection.cursor()
        query="INSERT INTO REVISION (ID,VEHICULO_ID,APROBADO,OBSERVACIONES,PERSONA_ID,FECHA_REVISION) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(
               request.json['idVehiculo'],
               request.json['aprobado'],
               request.json['Observaciones'],
               request.json['idPersona'],
               request.json['fechaRevision']

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
         'message': 'No existe Revision',
         'status':'False'}
          return jsonify(response)

        if(revi['idVehiculo'] != request.json['idVehiculo']):
          revi['idVehiculo']=request.json['idVehiculo']

        if(revi['aprobado'] != request.json['aprobado']):
          revi['aprobado']=request.json['aprobado']
        
        if(revi['Observaciones'] != request.json['Observaciones']):
          revi['Observaciones']=request.json['Observaciones']
        
        if(revi['idPersona'] != request.json['idPersona']):
          revi['idPersona']=request.json['idPersona']

        if(revi['fechaRevision'] != request.json['fechaRevision']):
          revi['fechaRevision']=request.json['fechaRevision']

        try:
           cursor = mySQLdb.connection.cursor()
           query="UPDATE REVISION SET VEHICULO_ID=%s,APROBADO=%s,OBSERVACIONES=%s,PERSONA_ID=%s,FECHA_REVISION=%s"
           cursor.execute(query,(
               request.json['idVehiculo'],
               request.json['aprobado'],
               request.json['Observaciones'],
               request.json['idPersona'],
               request.json['fechaRevision'],
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
         'message': 'No existe Revision',
         'status':'False'}
          return jsonify(response)

      try:
        cursor = mySQLdb.connection.cursor()
        query="DELETE FROM REVISION WHERE ID=%s"
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
      


    
    
    
    
    
    
