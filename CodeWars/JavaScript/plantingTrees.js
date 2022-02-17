/*
There is a rectangular land and we need to plant trees on the edges of that land.

I will give you three parameters:

width and length, two integers > 1 that represents the land's width and length;

gaps, an integer >= 0, that is the distance between two trees.

Return how many trees have to be planted, if you can't achieve a symmetrical layout(see Example 3) then return 0.

*/

function sc(width,length,gaps){
  let perimiter = width * 2 + length * 2 - 4,
      mod = gaps + 1;
  if (perimiter % mod === 0){
    return perimiter / mod;
  }
  return 0;
}