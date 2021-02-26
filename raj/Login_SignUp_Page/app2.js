const loginform = document.getElementById("loginform");

const func = async (e) => {
  e.preventDefault();
  console.log("login");
  const info = {
      email: document.getElementById('email').value,
      password:  document.getElementById('password').value,      
  } 
  console.log(info);

  const res = await fetch('http://localhost:3000/login', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      //mode: 'no-cors',
      body: JSON.stringify(info)
  })
  const data = await res.json();
  const msg = document.getElementById("response");
  msg.innerHTML = data.msg;
  console.log(data);
}

loginform.addEventListener('submit', func);