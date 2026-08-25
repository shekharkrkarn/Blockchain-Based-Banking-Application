import hashlib
import time

from flask import Flask, render_template, request

app=Flask(__name__)
class Register:
    def __init__(self,index,data,previous_hash,difficult=1):
        self.index=index
        self.timestamp=time.time()
        self.data=data
        self.previous_hash=previous_hash
        self.nonce = 0
        self.difficult = difficult
        self.hash = self.mine_block()

    def calculate_hash(self):
        content=str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)+str(self.nonce)
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self):
        target="0"* self.difficult

        print(f"Mining block{self.index}.")

        while True:
            new_hash=self.calculate_hash()
            if new_hash.startswith(target):
                print("new hash",new_hash)
                return new_hash
            else:
                self.nonce+=1

class Blockchain:
    def __init__(self):
        self.chain=[Register(0,"Genesis Block","0")]

    def add_block(self,data):
        last=self.chain[-1]
        new=Register(len(self.chain),data,last.hash)
        self.chain.append(new)

blockchain=Blockchain()

@app.route("/payment",methods=["POST"])
def register():
    Bank_Name=request.form["Bank_Name"]
    UPI_ID=request.form["UPI_ID"]
    Sender_Account=request.form["Sender_Account"]
    Transaction=request.form["Transaction"]
    Holder_Account=request.form["Holder_Account"]

    user_data={"Bank_Name":Bank_Name,"UPI_ID":UPI_ID,"Sender_Account":Sender_Account,"Transaction":Transaction,"Holder_Account":Holder_Account}

    blockchain.add_block(user_data)

    # return f"User {Bank_Name} registered and stored in blockchain!"
    return render_template("BankingApplication.html",chain=blockchain.chain)


@app.route("/")
def home():
    return render_template("BankingApplication.html")

if __name__=="__main__":
    app.run(debug=True)



