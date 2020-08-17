from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
mylist=[]
dfs=[]
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            files = request.files.getlist('file')
                          
            dfs.clear()
            
            for file in files:
                dfs.append(pd.read_csv(file.filename))
                                                                 
            df = pd.concat(dfs)
        
        except:
            return "file not uploaded"
            
        for i in range(len((df.iloc[:,0]))):
            
            SA=df.iloc[i,1]
            CP=df.iloc[i,2]
            TA=df.iloc[i,3]
            CN=df.iloc[i,4]
            PG=df.iloc[i,5]
            PF=df.iloc[i,6]
            
            if(TA>CP):
                PL=((TA-CP)*100)/CP
            elif(CP>TA):
                PL="-"+str(((CP-TA)*100)/CP)
                
            mylist.append([df.iloc[i,0],PL,TA,(CN+PG+PF)])
                
    return render_template('upload.html')
    
    
@app.route('/data')
def display():
    return render_template('data.html', mylist=mylist)
    
    
if __name__ == '__main__':
    app.run(debug=True)