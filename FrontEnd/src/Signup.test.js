import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import Signup from "./Signup";
import { render } from '@testing-library/react';
import { screen } from "@testing-library/react"
import renderer from 'react-test-renderer';


it('Trail Test', () => {
  expect(true).toBeTruthy();
});


it("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(
<BrowserRouter>
  <Signup />
</BrowserRouter>,
div
  );
  ReactDOM.unmountComponentAtNode(div);
})

describe("Text Check", () => {
  it("Renders component correctly", () => {
    render(<Signup/>);
    screen.getByText(/Team Formation Assistant/i).toBeInTheDocument();
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
