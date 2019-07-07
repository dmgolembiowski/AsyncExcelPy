class Editor extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: null
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('An essay was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          <textarea value={this.state.value} onChange={this.handleChange} placeholder = "# Python Editor (Upcoming Feature)  
# https://excelpy.com/ 
#
# Python functions use this kind of syntax:
#
#def customFunction(userInput):
#    a = userInput
#    if a == 'Hello World':
#        return a
#
#def first_cell_greater(cellRef1, cellRef2):
#    outcome = None 
#    if cellRef1 < cellRef2:
#        outcome = False
#    
#    # 'elif' means 'else if'
#    
#    elif cellRef1 > cellRef2:
#        outcome = True 
#    
#    else:
#        # Then, cellRef1 == cellRef2, so...
#        return outcome
#
#  def loop(array):
#      # Suppose `array` = 'A0:A4'
#      # Then Excelpy will interpret `array` as:
#      # array = ['A0', 'A1', 'A2', 'A3', 'A4']
#      loop_sum = 0
#      for cells in array:
#          loop_sum = loop_sum + cells
#      return loop_sum"/>
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

ReactDOM.render(
  <Editor />,
  document.getElementById('Editor')
);
