import React, { useState, useEffect } from 'react';
import ProductTable from './Components';

const SearchBar = ({
  filterText,
  inStockOnly,
  handleFilterTextChange,
  handleCheckBoxChange
}) => (
    <form>
      <input
        type="text"
        placeholder="Search..."
        value={filterText}
        onChange={handleFilterTextChange}
      />
      <p>
        <input
          type="checkbox"
          checked={inStockOnly}
          onChange={handleCheckBoxChange}
        />
        {' '}
      Only show products in stock
    </p>
    </form>
  );

const FilterableProductTable = () => {
  const [products, setProducts] = useState([])
  const [filterText, setFilterText] = useState('');
  const [inStockOnly, setInStockOnly] = useState(false);

  const handleFilterTextChange = (e) => setFilterText(e.target.value);
  const handleCheckBoxChange = (e) => setInStockOnly(e.target.checked);

  useEffect(() => {
    fetch('/products')
      .then((resp) => resp.json())
      .then(({ products }) => setProducts(products));
  }, []);
    return (
    <div>
      <SearchBar
        filterText={filterText}
        inStockOnly={inStockOnly}
        handleFilterTextChange={handleFilterTextChange}
        handleCheckBoxChange={handleCheckBoxChange}
      />
      <ProductTable
        products={products}
        filterText={filterText}
        inStockOnly={inStockOnly}
      />
    </div>
  )
}

export default FilterableProductTable;