const express = require("express");
const cors = require("cors");
const fs = require("fs").promises;

const app = express();

const port = 3000;

app.use(express.json());
app.use(cors({origin: 'http://127.0.0.1:5500'}));

app.get('/', (req,res) => {
  return res.send("Hello World");
})

app.post('/signup', async (req,res) => {
  console.log(req.body);
  // 1. get req body
  const obj = req.body
  // // 2. get json data

  const data = await fs.readFile('data.json');  
  // // // 3. push this new obj to json
  //console.log(data);
  const dataJson = JSON.parse(data);
  dataJson.push(obj);
  const parsedJson = JSON.stringify(dataJson);
  setTimeout(()=> {
    fs.writeFile('data.json', parsedJson);
  },2000);
  
  // // // 4. write data back to json file
  
  return res.status(200).send({msg: "Account Created Successfully"});
})

app.post('/login', async (req,res) => {
  console.log(req.body);
  
  // 1. get req body
  const obj = req.body;

  // 2. get json data
  const data = await fs.readFile('data.json');
  const dataJson = JSON.parse(data)

  // 3. search for the obj
  const query = dataJson.filter((x)=> x.email.toLowerCase()==obj.email.toLowerCase())
  // 4. verify the credentials
  console.log(query);
  if(query.length==0) return res.status(404).send({msg: "Email does not exist"});
  const acc = query[0];

  if(acc.password != obj.password) return res.status(400).send({msg: "Email or Password is incorrect"});

  // 5. return success or failure
  return res.status(200).send({msg: "Login Successful"});

})

// open localhost:3000

app.listen(port, ()=>{
  console.log(`Server is running on port ${port}`);
})