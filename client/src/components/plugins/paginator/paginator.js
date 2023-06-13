export function paginateArray(array, currentPage = 1, pageRows = 10) {
  const startIndex = (currentPage - 1) * pageRows;
  const endIndex = startIndex + pageRows;
  return array.slice(startIndex, endIndex);
}
