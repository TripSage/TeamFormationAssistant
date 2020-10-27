import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import {render} from "@testing-library/react";
import renderer from "react-test-renderer";


it('Trail Test', () => {
  expect(true).toBeTruthy();
});

it("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(
<BrowserRouter>
  <App />
</BrowserRouter>,
div
  );
  ReactDOM.unmountComponentAtNode(div);
})

describe('Fetch Team Data', () => {
  it('fetches data from server when server returns a successful response', done => { // 1
    const mockSuccessResponse = {};
    const mockJsonPromise = Promise.resolve(mockSuccessResponse); // 2
    const mockFetchPromise = Promise.resolve({ // 3
      json: () => mockJsonPromise,
    });
    jest.spyOn(global, 'fetch').mockImplementation(() => mockFetchPromise); // 4
    expect(global.fetch).toHaveBeenCalledTimes(1);
    expect(global.fetch).toHaveBeenCalledWith('http://localhost:5000/getResults');
  });
});


describe('Test suits for Home DOM Tree check', () => {
it('should match with snapshot', () => {
  const tree = renderer
  .create(
    <BrowserRouter>
    </BrowserRouter>
  )
  .toJSON();
 expect(tree).toBeNull();
 });
});

