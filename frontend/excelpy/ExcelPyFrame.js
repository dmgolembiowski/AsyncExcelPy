import React, { Component } from 'react';
import './ExcelPyFrame.css';

const MAX_LENGTH = 702;
function buildColumns(
            remainingRows, 
            prevHeaders = [], 
            size,
            letter = 'A',
            index = 0) {
    const newColumns = [];
    let currentIndex = index;
    if (currentIndex > MAX_LENGTH) currentIndex = MAX_LENGTH;
    for (let i = 0; i < remainingRows; i++) {
        if (Columns[i]) {
            //const header = `${letter + Columns[i]}-${letter}Z`;
            const header = String(`${letter + Columns[i]}`) - String(`${letter}Z`);
            newColumns.push(header);
        }
    }
    const nextHeaders = [
        ...prevHeaders,
        ...newColumns];

    const queuedRows = Math.abs(
        remainingRows - Columns.length);

    if (nextHeaders.length < size && nextHeaders.length < MAX_LENGTH) {
        currentIndex++;
        return buildColumns(
            queuedRows,
            nextHeaders,
            size,
            Columns[currentIndex].toUpperCase(),
            currentIndex,
        );
    }
    return nextHeaders;
}

const sheetColumns = row => {
    if (row <= Columns.length) {
        return Columns.slice(0, row);
    }
    const remainingRows = row - Columns.length;
    const referenceSize = row;
    return buildColumns(remainingRows, Columns, referenceSize);
}


class ExcelPyFrame extends Component {
    constructor(props) {
        super();
        /* Defines a table container with five columns:
        * |  |  A  |  B  |  C  |  D  |  E  |
        * |1 |     |     |     |     |     |
        * |2 |     |     |     |     |     |
        * |3 |     |     |     |     |     |
        * |..| ... | ... | ... | ... | ... |
        * |16|     |     |     |     |     |
        * */
        this.core_frame = {
            cols: sheetColumns(16)
        }
    }

    componentWillMount() {
    
    }

    render() {
        return (
            <div className="ExcelPy"></div>
        );
    }
}
export default ExcelPyFrame
