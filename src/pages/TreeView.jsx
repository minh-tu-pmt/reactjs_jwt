import React from "react";

const data = [
  {
    title: "Node 1",
    childNodes: [
      { title: "Childnode 1.1" },
      {
        title: "Childnode 1.2",
        childNodes: [
          {
            title: "Childnode 1.2.1",
            childNodes: [{ title: "Childnode 1.2.1.1" }],
          },
          { title: "Childnode 1.2.2" },
        ],
      },
    ],
  },
];

const TreeView = ({ data }) => {
  return (
    <div>
      <ul>
        {data &&
          data.map((item) => (
            <li>
              {item.title}
              {item.childNodes && <TreeView data={item.childNodes} />}
            </li>
          ))}
      </ul>
    </div>
  );
};

export default function Tree() {
  return (
    <div>
      <TreeView data={data} />
    </div>
  );
}
