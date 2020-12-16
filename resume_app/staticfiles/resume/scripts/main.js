
function addSkill () {
    const elements = document.getElementsByClassName('yui-u skills');
    let tag = document. createElement("div");
    tag.className = 'talent';
    tag.innerHTML = `
      <input class="skillname" type="text" placeholder="Your Skill Name">
      <input type="button" value="x" class = "myButton" onclick="remove('yui-u skills',this)">
      <textarea class="skilltext" name="" id="" cols="22" rows="10"
        placeholder="Skill Description"></textarea>
      
    `;
    elements[0].appendChild(tag);
}


function addTechnical() {
    const arrforpick = ['Adobe Illustrator','css','html','Adobe Photoshop','Js','Python','WordPress'];
    let rand = Math.random();
    rand *= arrforpick.length;
    rand = Math.floor(rand);
    console.log(rand);
    const elements = document.getElementsByClassName('yui-u Technical');
    let tag = document.createElement("div");
    tag.className = 'talent';
    tag.innerHTML = `
      <input type="text" placeholder = "skill e.g ${arrforpick[rand]}"></input>
      <input type="button" class="myButton" value="x" onclick="remove('yui-u Technical',this)"></input>
    `;
    elements[0].appendChild(tag);
}



function addJob() {
  const elements = document.getElementsByClassName('yui-u Experience');
  let tag = document.createElement("div");
  tag.className = 'job';
  tag.innerHTML = `
      <h2><input type="text" placeholder="Company"></h2>
      <h3><input type="text" placeholder="Position"></h3>
      <h4><input type="text" placeholder="e.g Jul 2020 - Feb 2022"></h4>
      <textarea cols="60" rows="4" style="resize: none;" placeholder = "About Work"></textarea>
      <input class="myMinusButton" type="button" value="x" onclick="remove('yui-u Experience',this)">

  `;
  elements[0].appendChild(tag);
}


function addEducation() {
    const elements = document.getElementsByClassName('yui-gf Education last');
    let tag = document.createElement("div");
    tag.className = 'yui-u';
    tag.innerHTML = `
      <input class="myButton" type="button" value="x" onclick="remove('yui-gf Education last',this)">
      <h2><input type="text" placeholder="Education place"></h2>
      <h3><input type="text" placeholder="Education field"> &mdash; <strong><input type="text" placeholder="1-4 gpa"> GPA</strong> </h3>
    `;
    elements[0].appendChild(tag);
}


function remove(classname,input) {
  document.getElementsByClassName(classname)[0].removeChild(input.parentNode);
}
