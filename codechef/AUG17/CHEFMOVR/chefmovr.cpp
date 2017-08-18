#include <iostream>
using namespace std;

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);

    int t, n, d, ans, sum, sub_n;
    int *arr = new int[n];

    cin >> t;
    while(t--) {
        cin >> n >> d;
        for(int i=0; i<n; i++) {
            cin >> arr[i];
        }

        ans = -1;
        for(int i=0; i<d; i++) {
            sum = 0;
            sub_n = 0;
            for(int j=i; j<n; j=j+d) {
                sum += arr[j];
                sub_n += 1;
            }

            if(sum%sub_n == 0) {
                if(ans == -1){
                    ans = sum/sub_n;
                } else if(ans != sum/sub_n) {
                    ans = -1;
                    break;
                }
            } else {
                ans = -1;
            }
        }

        cout << ans << "\n";
    }

    return 0;
}
