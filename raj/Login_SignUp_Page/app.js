const signupform = document.getElementById("signupform");

const func= async (e) => {
   e.preventDefault();
   const info={
          firstName: document.getElementById('first_name').value,
          lastName:  document.getElementById('last_Name').value,
          email:     document.getElementById('Email').value,
          password:  document.getElementById('password').value,
          gender:    document.getElementById('gender').value,
          day: document.getElementById('DOB_day').value,
          month: document.getElementById('DOB_month').value,
          year: document.getElementById('DOB_year').value
    } 
    //const obj = {name: 'test'}
    console.log(info);

    const res = await fetch('http://localhost:3000/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        //mode: 'no-cors',
        body: JSON.stringify(info)
    })

    const data = await res.json();

    const msg = document.getElementById("res");

    msg.innerHTML = data.msg;
    console.log(data);
}


signupform.addEventListener('submit', func);


