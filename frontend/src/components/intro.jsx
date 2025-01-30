const Intro = () => {
  return (
    <div className="hero bg-base-200 min-h-screen">
      <div className="hero-content lg:flex-row-reverse min-w-3xl">
        <div className="card bg-base-100 w-full max-w-sm shrink-0 shadow-2xl">
          <div className="card-body">
            <fieldset className="fieldset min-w-full">
              <div>
                <label className="fieldset-label my-3">WEB Address:</label>
                <input
                  type="text"
                  className="input"
                  placeholder="WEB ADDRESS"
                />
                <label className="fieldset-label mt-4">Custom Short Link:</label>
                <input
                  type="text"
                  className="input my-3"
                  placeholder="Your Unique Short Link"
                />

                <button className="btn btn-neutral mt-4 w-full">
                  Generate
                </button>
              </div>
            </fieldset>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Intro;
