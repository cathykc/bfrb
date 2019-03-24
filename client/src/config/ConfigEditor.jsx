import * as React from 'react';
import { Card, Input, Checkbox, Form, Button, Icon } from 'semantic-ui-react';
import './ConfigEditor.css';
import _ from 'lodash';

const getDefaultQuestion = idx => {
  return {
    prompt_key: '',
    prompt_text: '',
    prompt_type: 'text',
  };
};

export default class ConfigEditor extends React.Component {
  constructor(props) {
    super(props);
    this.state = { config: props.initialConfig || [] };
  }

  // im sorry
  componentWillReceiveProps(nextProps) {
    this.setState({ config: nextProps.initialConfig || [] });
  }

  state = {
    config: [],
  };

  editQuestion = (idx, data) => {
    let newConfig = _.cloneDeep(this.state.config);
    newConfig[idx] = {
      ...newConfig[idx],
      ...data,
    };
    this.setState({ config: newConfig });
  };

  addQuestion = () => {
    this.setState({
      config: this.state.config.concat([
        getDefaultQuestion(this.state.config.length),
      ]),
    });
  };

  deleteQuestion = idx => {
    let newConfig = _.cloneDeep(this.state.config);
    newConfig.splice(idx, 1);
    this.setState({ config: newConfig });
  };

  saveConfig = () => {
    // Clean up comma-separated values into lists, and remove
    // "draft" response_options if the prompt_type isn't "choice"
    const tidyConfig = this.state.config.map(question => {
      let tidyQuestion = {
        prompt_key: question.prompt_key,
        prompt_text: question.prompt_text,
        response_type: question.response_type,
      };
      if (question.response_type === 'choice') {
        tidyQuestion.response_options = _(question.response_options)
          .split(',')
          .map(option => _.trim(option))
          .value();
      }
      return tidyQuestion;
    });

    this.props.onChange(tidyConfig);
  };

  render() {
    const { config } = this.state;

    return (
      <div className="ConfigEditor">
        {config.map((question, idx) => (
          <Card key={idx} className="question-card">
            <Card.Content>
              <Card.Header>
                <Input
                  className="question-prompt-text editable-underline"
                  placeholder="What is your name?"
                  value={question.prompt_text}
                  onChange={event =>
                    this.editQuestion(idx, {
                      prompt_text: event.target.value,
                    })
                  }
                />
              </Card.Header>
              <Form>
                <Form.Field>
                  <Checkbox
                    toggle={true}
                    label="Multiple choice"
                    checked={question.response_type === 'choice'}
                    onChange={() => {
                      const newType =
                        question.response_type === 'choice' ? 'text' : 'choice';
                      this.editQuestion(idx, {
                        response_type: newType,
                      });
                    }}
                  />
                </Form.Field>
                {question.response_type === 'choice' && (
                  <Form.Field inline={true} style={{ marginBottom: '0.6em' }}>
                    <label>Options:</label>
                    <Input
                      style={{ marginBottom: 3 }}
                      className="editable-underline"
                      transparent={true}
                      placeholder="first, second, third"
                      value={question.response_options}
                      onChange={event =>
                        this.editQuestion(idx, {
                          response_options: event.target.value,
                        })
                      }
                    />
                  </Form.Field>
                )}
                <Form.Field inline={true}>
                  <label>Question ID:</label>
                  <Input
                    style={{ marginBottom: 3 }}
                    className="editable-underline"
                    transparent={true}
                    placeholder="e.g. urge_strength"
                    value={question.prompt_key}
                    onChange={event =>
                      this.editQuestion(idx, {
                        prompt_key: event.target.value,
                      })
                    }
                  />
                </Form.Field>
              </Form>
            </Card.Content>
            <div className="delete-button">
              <Button
                basic={true}
                icon={true}
                onClick={() => this.deleteQuestion(idx)}
              >
                <Icon name="trash" />
              </Button>
            </div>
          </Card>
        ))}
        <Button
          basic={true}
          onClick={this.addQuestion}
          className="new-question-button"
        >
          Add question
        </Button>
        <br />
        <br />
        <Button primary={true} onClick={this.saveConfig}>
          Save flow
        </Button>
      </div>
    );
  }
}
