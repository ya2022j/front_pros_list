
### html+css模仿微信对话聊天布局

* 以下是一个简单的HTML和CSS代码示例，可用于模仿微信对话聊天布局。


```shell

<html>
            <head>
<style>
            .chat-container {
  display: flex;
  flex-direction: column;
  height: 500px;
  border: 1px solid #ccc;
  padding: 10px;
}

.chat-message {
  display: flex;
  margin: 5px 0;
}

.received {
  justify-content: flex-start;
}

.sent {
  justify-content: flex-end;
}

.message-content {
  background-color: #fff;
  border-radius: 5px;
  padding: 10px;
  max-width: 70%;
}

.sent .message-content {
  background-color: #dcf8c6;
}

.received .message-content {
  background-color: #f6f6f6;
}

.message-content p {
  margin: 0;
  font-size: 14px;
}
</style>
            </head>


            <body>
                        <div class="chat-container">
                                    <div class="chat-message received">
                                      <div class="message-content">
                                        <p>Hello! How are you doing?</p>
                                      </div>
                                    </div>
                                    <div class="chat-message sent">
                                      <div class="message-content">
                                        <p>Hi there! I'm doing great, thanks for asking.</p>
                                      </div>
                                    </div>
                                    <div class="chat-message received">
                                      <div class="message-content">
                                        <p>That's good to hear. How's your day been?</p>
                                      </div>
                                    </div>
                                  </div>
            </body>
</html>

```
说明：

* 通过使用 flex 布局，将聊天消息容器的方向设置为垂直（列）方向，并设置其高度和内边距。
* 使用 .chat-message 类来定义聊天消息的样式，将其展示为 flex 容器，并设置上下边距。
* 使用 .received 类和 .sent 类来定义不同的消息类型，以便左右对齐聊天消息。
* 使用 .message-content 类来定义消息内容区域的样式，包括背景颜色、圆角、内边距和最大宽度。
* 根据消息类型使用不同的背景颜色，以便区分发送和接收消息。
* 通过设置段落元素的外边距为 0，使聊天消息更紧凑和整洁。
* 这是一个简单的示例，可以根据需要进行进一步的自定义和改进。
