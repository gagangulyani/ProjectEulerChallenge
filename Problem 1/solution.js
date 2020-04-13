function multiplesOf3and5(number) {
    let sum_ = 0;
  
    for (var i=2; i < number; i++){
        if (i % 3 === 0 || i % 5 === 0){
            sum_ += i;
        }
    }
    return sum_;
  }
  
  var result = multiplesOf3and5(1000);

  console.log(result);