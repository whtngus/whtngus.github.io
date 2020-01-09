# 한국어 임베딩 6장 - 1 2 코드 설명대로 주석 추가

class Tuner(object):

    def __init__(self, train_corpus_fname=None, tokenized_train_corpus_fname=None,
                 test_corpus_fname=None, tokenized_test_corpus_fname=None,
                 model_name="bert", model_save_path=None, vocab_fname=None, eval_every=1000,
                 batch_size=32, num_epochs=10, dropout_keep_prob_rate=0.9, model_ckpt_path=None,
                 sp_model_path=None):
        '''
        하이퍼파라미터 설정값 들을 저장
        :param train_corpus_fname:
        :param tokenized_train_corpus_fname:
        :param test_corpus_fname:
        :param tokenized_test_corpus_fname:
        :param model_name: 어떤 모델을 사용할 지
        :param model_save_path:
        :param vocab_fname:
        :param eval_every: 평가 주기
        :param batch_size: 배치 사이즈 크기
        :param num_epochs: 학습 에폭 수
        :param dropout_keep_prob_rate: 드롭아웃 비율
        :param model_ckpt_path:
        :param sp_model_path:
        '''
        # configurations
        tf.logging.set_verbosity(tf.logging.INFO)
        self.model_name = model_name
        self.eval_every = eval_every
        self.model_ckpt_path = model_ckpt_path
        self.model_save_path = model_save_path
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.dropout_keep_prob_rate = dropout_keep_prob_rate
        self.best_valid_score = 0.0
        if not os.path.exists(model_save_path):
            os.mkdir(model_save_path)
        # define tokenizer
        if self.model_name == "bert":
            self.tokenizer = FullTokenizer(vocab_file=vocab_fname, do_lower_case=False)
        elif self.model_name == "xlnet":
            sp = spm.SentencePieceProcessor()
            sp.Load(sp_model_path)
            self.tokenizer = sp
        else:
            self.tokenizer = get_tokenizer("mecab")
        # load or tokenize corpus
        self.train_data, self.train_data_size = self.load_or_tokenize_corpus(train_corpus_fname, tokenized_train_corpus_fname)
        self.test_data, self.test_data_size = self.load_or_tokenize_corpus(test_corpus_fname, tokenized_test_corpus_fname)

    def load_or_tokenize_corpus(self, corpus_fname, tokenized_corpus_fname):
        '''
        말뭉치 로드 및 형태소 분석 함수 
        - 클래스가 선엄됭과 동시에 호출 ( __init__ 에서 호출하기 때문에)
        :param corpus_fname: tokenized_corpus_fname에 데이터가 없는경우 해당경로에서 데이터를 읽어 형태소 분석 실시
        :param tokenized_corpus_fname: 경로에 데이터가 존재하면 해당 데이터를 읽어들임
        :return:
        '''
        data_set = []
        if os.path.exists(tokenized_corpus_fname):
            tf.logging.info("load tokenized corpus : " + tokenized_corpus_fname)
            with open(tokenized_corpus_fname, 'r') as f1:
                for line in f1:
                    tokens, label = line.strip().split("\u241E")
                    if len(tokens) > 0:
                        data_set.append([tokens.split(" "), int(label)])
        else:
            tf.logging.info("tokenize corpus : " + corpus_fname + " > " + tokenized_corpus_fname)
            with open(corpus_fname, 'r') as f2:
                next(f2)  # skip head line
                for line in f2:
                    sentence, label = line.strip().split("\u241E")
                    if self.model_name == "bert":
                        tokens = self.tokenizer.tokenize(sentence)
                    elif self.model_name == "xlnet":
                        normalized_sentence = preprocess_text(sentence, lower=False)
                        tokens = encode_pieces(self.tokenizer, normalized_sentence, return_unicode=False, sample=False)
                    else:
                        tokens = self.tokenizer.morphs(sentence)
                        tokens = post_processing(tokens)
                    if int(label) > 0.5:
                        int_label = 1
                    else:
                        int_label = 0
                    data_set.append([tokens, int_label])
            with open(tokenized_corpus_fname, 'w') as f3:
                for tokens, label in data_set:
                    f3.writelines(' '.join(tokens) + "\u241E" + str(label) + "\n")
        return data_set, len(data_set)

    def train(self, sess, saver, global_step, output_feed):
        '''
        학습을 수행
        파라미터는 Tuner를 상속받는 자식 클래스에서 각자 정의해서 쓸 수 있도록 여지를 남겨둠
        ELMO ADMA   MERT 웜업 기반의 아담 옵티마이저 
        :param sess: 
        :param saver: 
        :param global_step: 
        :param output_feed: 
        :return: 
        '''
        train_batches = self.get_batch(self.train_data, num_epochs=self.num_epochs, is_training=True)
        checkpoint_loss = 0.0
        for current_input_feed in train_batches:
            _, _, _, current_loss = sess.run(output_feed, current_input_feed)
            checkpoint_loss += current_loss
            if global_step.eval(sess) % self.eval_every == 0:
                tf.logging.info("global step %d train loss %.4f" %
                                (global_step.eval(sess), checkpoint_loss / self.eval_every))
                checkpoint_loss = 0.0
                self.validation(sess, saver, global_step)

    def validation(self, sess, saver, global_step):
        '''
        사용자가 지정한 스텝 수 (eval_every)를 만족하면 모델을 평가
        테스트 데이터를 전체 1회 평가
        :param sess: 
        :param saver: 
        :param global_step: 
        :return: 
        '''
        valid_loss, valid_pred, valid_num_data = 0, 0, 0
        output_feed = [self.logits, self.loss]
        test_batches = self.get_batch(self.test_data, num_epochs=1, is_training=False)
        for current_input_feed, current_labels in test_batches:
            current_logits, current_loss = sess.run(output_feed, current_input_feed)
            current_preds = np.argmax(current_logits, axis=-1)
            valid_loss += current_loss
            valid_num_data += len(current_labels)
            for pred, label in zip(current_preds, current_labels):
                if pred == label:
                    valid_pred += 1
        valid_score = valid_pred / valid_num_data
        tf.logging.info("valid loss %.4f valid score %.4f" %
                        (valid_loss, valid_score))
        if valid_score > self.best_valid_score:
            self.best_valid_score = valid_score
            path = self.model_save_path + "/" + str(valid_score)
            saver.save(sess, path, global_step=global_step)

    def get_batch(self, data, num_epochs, is_training=True):
        '''
        어떤 임베딩을 쓰더라도 배치 데이터를 생성하는 과정은 같음
        사용자 지정 에폭수만큼 배치를 지정 
        :param data:
        :param num_epochs:
        :param is_training:
        :return:
        '''
        if is_training:
            data_size = self.train_data_size
        else:
            data_size = self.test_data_size
        num_batches_per_epoch = int((data_size - 1) / self.batch_size)
        if is_training:
            tf.logging.info("num_batches_per_epoch : " + str(num_batches_per_epoch))
        for epoch in range(num_epochs):
            idx = random.sample(range(data_size), data_size)
            data = np.array(data)[idx]
            for batch_num in range(num_batches_per_epoch):
                batch_sentences = []
                batch_labels = []
                start_index = batch_num * self.batch_size
                end_index = (batch_num + 1) * self.batch_size
                features = data[start_index:end_index]
                for feature in features:
                    sentence, label = feature
                    batch_sentences.append(sentence)
                    batch_labels.append(int(label))
                yield self.make_input(batch_sentences, batch_labels, is_training)

    def make_input(self, sentences, labels, is_training):
        '''
        입렵값을 생성
        :param sentences: 
        :param labels: 
        :param is_training: 
        :return: 
        '''
        raise NotImplementedError

    def tune(self):
        '''
        옵티마이저 등을 정하는 함수
        :return:
        '''
        raise NotImplementedError


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, help='model name')
    parser.add_argument('--train_corpus_fname', type=str, help='train corpus file name')
    parser.add_argument('--test_corpus_fname', type=str, help='test corpus file name')
    parser.add_argument('--vocab_fname', type=str, help='vocab file name')
    parser.add_argument('--pretrain_model_fname', type=str, help='pretrained model file name')
    parser.add_argument('--config_fname', type=str, help='config file name')
    parser.add_argument('--model_save_path', type=str, help='model save path')
    parser.add_argument('--embedding_name', type=str, help='embedding name')
    parser.add_argument('--embedding_fname', type=str, help='embedding file path')
    parser.add_argument('--num_gpus', type=str, help='number of GPUs (XLNet only)')
    args = parser.parse_args()