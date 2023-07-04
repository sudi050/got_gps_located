function openForm() {
    document.getElementById("myForm").style.display = "block";
    console.log("openForm");
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  } 

  function swap(option) {
    const cars = document.querySelectorAll('.car');
    cars.forEach((car) => {
        car.classList.remove('selected');
    });

    const selectedCar = document.getElementById(option);
    selectedCar.classList.add('selected');
    document.getElementById('mode').innerHTML = option;
}