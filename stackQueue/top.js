function solution(heights) {
  var answer = [];
  for (let i = heights.length; i >= 0; i--) {
    let value = heights[i];
    let tempArr = heights.slice(0, i);

    console.log(value, tempArr);
  }
  //   return answer;
}

solution([6, 9, 5, 7, 4]);
