class interpreterDB():
    
    def Select(values,table,filter):
        SelectCon="select {values} from {table} where {filter}".format(
            values=values,table=table,filter=filter
        )
        return SelectCon   
    
    def Select(values,table):
        SelectCon="select {values} from {table}".format(
            values=values,table=table
        )
        return SelectCon
    
    def UnionSim(tables,values):
        UnionCon="select {values} from {table}".format(
            values=values, table=tables[0]
        )
        for table in tables[1:]:
            UnionCon+="union select {values} from {table}".format(
                values=values,table=table)  
        return UnionCon
    def Insert(table,values):
        InsertCon="insert into {table} values {values}".format(
            table=table,values=values
        )
        return InsertCon
    def Create(table,values):
        CreateCon="CREATE TABLE IF NOT EXISTS {table} ({values})".format(
            table=table,values=values) 
        return CreateCon      
        


##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
