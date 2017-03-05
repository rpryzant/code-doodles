var ItemView = React.createClass({

  getInitialState: function() {
    return {
      error: false,
      percent: null,
    };
  },

  componentDidMount: function() {
    this.getData();
  },

  getData: function() {
    $.getJSON('/item/' + this.props.item)
      .done(function(data) {
        this.setState({data: data.values});
      }.bind(this)).fail(function() {
        this.setState({error: true});
      }.bind(this));
  },

  render: function() {
    var error;
    if (this.state.error) {
      error = <p>An error occured when making the request</p>;
    }

    var percent_text;
    if (this.state.data != null) {
      percent_text = (this.state.data[this.state.data.length - 1][1] * 100).toFixed(0)
    }

    return (
      <div className="item-view">
        {error}
        {this.props.item} <br /> <br /> <br /> <span className="percent-style">{percent_text}%</span>
      </div>

    );
  },

});
